# api/routes_wifi.py
from fastapi import APIRouter
from typing import Dict, Any

router = APIRouter(prefix="/wifi", tags=["wifi"])
WIRELESS_STATS = {
    "probe_requests": 0,
    "rogue_aps": [],
    "channels_seen": []
}

@router.get("/dashboard")
def wifi_dashboard() -> Dict[str, Any]:
    """
    """
    return WIRELESS_STATS
