from fastapi import APIRouter

router = APIRouter()

@router.get("/callback")
def oauth_callback():
    return {"message": "OAuth callback endpoint"}
