from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="/health_check", tags=["health_check"])


@router.post("", status_code=200)
async def health_check():
    return PlainTextResponse(content="Health check done", status_code=200)
