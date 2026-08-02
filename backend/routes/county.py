from fastapi import APIRouter
from dashboard.services.county_service import (
    dashboard_summary,
    county
)

router = APIRouter()


@router.get("/summary")
def summary():
    return dashboard_summary()


@router.get("/county/{county_name}")
def county_info(county_name: str):
    return county(county_name)

