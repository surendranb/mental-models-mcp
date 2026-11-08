# SPDX-License-Identifier: MIT
"""Fleet-wide update checker for mental-models-mcp."""
from __future__ import annotations
import json
import re
import threading
import time
import urllib.request
from pathlib import Path
from typing import Any, Dict

_FLEET_CACHE_FILE = Path.home() / ".cache" / "mcp_fleet_updates.json"
_UPDATE_CHECK_TTL = 86400  # 24 hours
_NUDGE_THROTTLE_INTERVAL = 7 * 86400  # 7 days per version


def _parse_version(v: str) -> tuple[int, ...]:
    try:
        clean = re.sub(r"[^\d.]", "", v)
        return tuple(int(p) for p in clean.split(".") if p.isdigit())
    except Exception:
        return (0,)


def check_server_update(package_name: str, current_version: str, force_check: bool = False) -> Dict[str, Any]:
    """Checks PyPI for latest version and returns update status and instructions."""
    now = time.time()
    cache: Dict[str, Any] = {}
    if _FLEET_CACHE_FILE.exists():
        try:
            cache = json.loads(_FLEET_CACHE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass

    entry = cache.get(package_name, {})
    last_check = entry.get("last_checked", 0)
    latest_version = entry.get("latest_version", current_version)

    if force_check or (now - last_check > _UPDATE_CHECK_TTL):
        try:
            req = urllib.request.Request(
                f"https://pypi.org/pypi/{package_name}/json",
                headers={"User-Agent": f"{package_name}/{current_version}"},
            )
            with urllib.request.urlopen(req, timeout=2.5) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                latest_version = data.get("info", {}).get("version", current_version)
                entry["latest_version"] = latest_version
                entry["last_checked"] = now
                cache[package_name] = entry
                _FLEET_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
                tmp = _FLEET_CACHE_FILE.with_suffix(".tmp")
                tmp.write_text(json.dumps(cache), encoding="utf-8")
                tmp.replace(_FLEET_CACHE_FILE)
        except Exception:
            pass

    has_update = _parse_version(latest_version) > _parse_version(current_version)
    cmd = f"uvx --refresh {package_name}"
    msg = (
        f"An updated version of {package_name} is available (v{latest_version}, current: v{current_version}). "
        f"Inform the user to run '{cmd}' to update. Do NOT attempt to run this command yourself in this session."
        if has_update
        else f"{package_name} is up to date (v{current_version})."
    )
    return {
        "server": package_name,
        "current_version": current_version,
        "latest_version": latest_version,
        "update_available": has_update,
        "upgrade_command": cmd if has_update else None,
        "message": msg,
    }


def get_upgrade_nudge(package_name: str, current_version: str) -> str:
    """Returns in-band upgrade directive if outdated, else empty string. Non-blocking."""
    try:
        now = time.time()
        cache: Dict[str, Any] = {}
        if _FLEET_CACHE_FILE.exists():
            try:
                cache = json.loads(_FLEET_CACHE_FILE.read_text(encoding="utf-8"))
            except Exception:
                pass

        entry = cache.get(package_name, {})
        last_check = entry.get("last_checked", 0)
        latest_version = entry.get("latest_version", current_version)
        last_nudged = entry.get("last_nudged", 0)

        if now - last_check > _UPDATE_CHECK_TTL:
            def _fetch():
                try:
                    req = urllib.request.Request(
                        f"https://pypi.org/pypi/{package_name}/json",
                        headers={"User-Agent": f"{package_name}/{current_version}"},
                    )
                    with urllib.request.urlopen(req, timeout=2.5) as resp:
                        data = json.loads(resp.read().decode("utf-8"))
                        ver = data.get("info", {}).get("version", current_version)
                        c = {}
                        if _FLEET_CACHE_FILE.exists():
                            try:
                                c = json.loads(_FLEET_CACHE_FILE.read_text(encoding="utf-8"))
                            except Exception:
                                pass
                        e = c.get(package_name, {})
                        e["latest_version"] = ver
                        e["last_checked"] = time.time()
                        c[package_name] = e
                        _FLEET_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
                        tmp = _FLEET_CACHE_FILE.with_suffix(".tmp")
                        tmp.write_text(json.dumps(c), encoding="utf-8")
                        tmp.replace(_FLEET_CACHE_FILE)
                except Exception:
                    pass

            t = threading.Thread(target=_fetch, daemon=True)
            t.start()

        if _parse_version(latest_version) > _parse_version(current_version):
            if now - last_nudged > _NUDGE_THROTTLE_INTERVAL:
                entry["last_nudged"] = now
                cache[package_name] = entry
                try:
                    _FLEET_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
                    tmp = _FLEET_CACHE_FILE.with_suffix(".tmp")
                    tmp.write_text(json.dumps(cache), encoding="utf-8")
                    tmp.replace(_FLEET_CACHE_FILE)
                except Exception:
                    pass
                return (
                    f"\n\n[NOTICE: An update for {package_name} is available: v{latest_version} "
                    f"(current: v{current_version}). Upgrade command: 'uvx --refresh {package_name}']"
                )
    except Exception:
        pass
    return ""


def append_upgrade_nudge(package_name: str, current_version: str, out_str: str) -> str:
    nudge = get_upgrade_nudge(package_name, current_version)
    if not nudge:
        return out_str
    try:
        data = json.loads(out_str)
        if isinstance(data, dict):
            data["_upgrade_notice"] = nudge.strip()
            return json.dumps(data, indent=2)
    except Exception:
        pass
    return out_str + nudge
