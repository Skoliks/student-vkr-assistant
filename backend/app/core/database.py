from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from collections.abc import AsyncGenerator

from app.core.config import settings


engine = create_async_engine(url=settings.database_url, echo=settings.debug)

async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session