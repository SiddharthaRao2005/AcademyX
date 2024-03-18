from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from backend import settings
from backend.models.models import *
from sqlmodel import SQLModel
async_engine = create_async_engine(
   settings.database_uri,
   echo=True,
   future=True,
)

async_session = async_sessionmaker(
    bind= async_engine,
    class_=AsyncSession,
)

async def create_db() -> None:
    async with async_engine.begin() as conn:
        try:
         await conn.run_sync(SQLModel.metadata.create_all)
         print("Done!!!")
        except Exception as e:
            print(e)

async def get_async_session() -> AsyncGenerator[AsyncSession,None]:
   async with async_session() as session:
       yield session