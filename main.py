from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated
from services.ors import get_route

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Trip Planner API!",
        "usage": "POST to /trip/plan with source and destination coordinates."
    }


class Coordinate(BaseModel):
    latitude: Annotated[float, Field(..., ge=-90, le=90)]
    longitude: Annotated[float, Field(..., ge=-180, le=180)]


class TripRequest(BaseModel):
    source: Coordinate
    destination: Coordinate


@app.post("/trip/plan")
async def plan_trip(data: TripRequest):
    try:
        route_info = await get_route(
            {"latitude": data.source.latitude, "longitude": data.source.longitude},
            {"latitude": data.destination.latitude, "longitude": data.destination.longitude}
        )
        return {
            "status": "success",
            "route": route_info
        }
    except Exception as e:
        print(f"🔥 Internal error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
