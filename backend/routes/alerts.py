from fastapi import APIRouter
from backend.services.ai_center import system_state
from backend.services.fire_monitor import check_kenya_fire

router = APIRouter()

@router.get("/alerts")
def alerts():
    return system_state


@router.get("/test-fire")
def test_fire():
    return check_kenya_fire()