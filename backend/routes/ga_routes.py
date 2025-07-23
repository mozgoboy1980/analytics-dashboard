from fastapi import APIRouter

router = APIRouter()

@router.get("/ga/data")
def get_data():
    return {"visits": [100, 150, 200]}
