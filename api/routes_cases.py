# api/routes_cases.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/cases", tags=["cases"])

# Example case model
class Case(BaseModel):
    id: str
    title: str
    status: str
    severity: str
    description: Optional[str] = None


CASES_DB = []

@router.get("/", response_model=List[Case])
def list_cases():
    return CASES_DB

@router.post("/", response_model=Case)
def create_case(case: Case):
    CASES_DB.append(case)
    return case

@router.get("/{case_id}", response_model=Case)
def get_case(case_id: str):
    for c in CASES_DB:
        if c.id == case_id:
            return c
    return {"error": "no case was detected for this id"}

@router.delete("/{case_id}")
def delete_case(case_id: str):
    global CASES_DB
    CASES_DB = [c for c in CASES_DB if c.id != case_id]
    return {"status": "deleted", "id": case_id}
