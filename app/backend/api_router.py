from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/api/ping")
async def ping():
    return {"message": "pong"}