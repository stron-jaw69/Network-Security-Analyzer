from fastapi import APIRouter
from pydantic import BaseModel
from processing.soar import run_playbook

router = APIRouter(prefix="/soar")

class Event(BaseModel):
    event: str
    src_ip: str | None = None

@router.post("/run")
def run(event: Event):
    run_playbook(event.dict())
    return {"status": "executed"}
