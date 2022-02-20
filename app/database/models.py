from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database.db_admin import Base


class Entry(Base):
    """
    Table to store the items of the to-do list.
    """

    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
