# database.py
## === app/db/database.py ===
import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.settings import settings

engine = create_async_engine(
    settings.DATABASE_URL, 
    pool_size = settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    pool_pre_ping=True,
    pool_recycle=3600
    # connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)


AsyncSessionLocal = sessionmaker(engine,
                                 class_=AsyncSession,
                                 expire_on_commit=False
                                 )


async def get_db():
    async with AsyncSessionLocal() as session: 
        try: 
            yield session 
        finally: 
            await session.close() 