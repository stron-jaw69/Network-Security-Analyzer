# api/routes_stats.py

from fastapi import APIRouter

router = APIRouter(prefix="/stats")

@router.get("/bandwidth")
def bandwidth():
    return {"bandwidth_bps": 12345}
