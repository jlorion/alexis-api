from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session 
from sqlmodel.ext.asyncio.session import AsyncSession
from config.envi import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL, 
    echo=True,
    pool_size=5,              
    max_overflow=2,           
    connect_args={"statement_cache_size": 0},
)

async def getDatabaseSesssion():
    async with AsyncSession(engine) as session:
        try:
            yield session
        finally:
            await session.close()
