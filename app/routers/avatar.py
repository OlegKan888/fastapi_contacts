from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_avatar():
    return {"message": "Avatar endpoint is working"}
