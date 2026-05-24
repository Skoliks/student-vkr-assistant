from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.core.database import get_db

router = APIRouter(prefix="/health")


@router.get("")
def checking_app_work() -> dict:
    return {"status": "ok"}


@router.get("/db")
async def check_db(db: AsyncSession = Depends(get_db)) -> dict:
    result = await db.execute(text("SELECT 1"))
    value = result.scalar_one()
    
    return {
        "status": "ok",
        "database": "connected",
        "result": value
    }
