from fastapi import APIRouter

from backend.services.weather import get_weather
from backend.services.earthquake import get_earthquakes
from backend.services.wildfire import get_wildfires



router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.get("/weather")
def weather():
    return get_weather()


@router.get("/earthquakes")
def earthquakes():
    return get_earthquakes()
    

@router.get("/wildfires")
def wildfires():
    return get_wildfires()