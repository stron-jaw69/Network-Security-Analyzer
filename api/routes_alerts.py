# api/routes_alerts.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/alerts", tags=["alerts"])

# alert model
class Alert(BaseModel):
    id: str
    event: str
    severity: str
    src_ip: Optional[str] = None
    score: Optional[float] = None

# temp in-memory alert store
ALERTS_DB = []

@router.get("/", response_model=List[Alert])
def list_alerts():
    return ALERTS_DB

@router.post("/", response_model=Alert)
def create_alert(alert: Alert):
    ALERTS_DB.append(alert)
    return alert

@router.get("/{alert_id}", response_model=Alert)
def get_alert(alert_id: str):
    for a in ALERTS_DB:
        if a.id == alert_id:
            return a
    return {"error": "--no alerts found--"}

@router.delete("/{alert_id}")
def delete_alert(alert_id: str):
    global ALERTS_DB
    ALERTS_DB = [a for a in ALERTS_DB if a.id != alert_id]
    return {"status": "deleted alert ", "id": alert_id}
