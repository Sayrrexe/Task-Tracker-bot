from sqlalchemy import ForeignKey, String, BigInteger, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import DB_URL

engine = create_async_engine(url=DB_URL,
                             echo=True)
    
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    phone = mapped_column(BigInteger)
    user_name = mapped_column(String(50), nullable=True)
    Approved: Mapped[int] = mapped_column(default=1)
    
class TasksTable(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String(100), nullable=False)
    text = Column(String(500), nullable=False)  # Текст задания
    due_date = Column(String(15), nullable=False)
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
