from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime

from app.database.database import Base


class Entry(Base):
	"""
	Table to store the items of the to-do list.
	"""
	__tablename__ = 'entries'

	id = Column(Integer, primary_key=True)
	time_created = Column(DateTime(timezone=True), server_default=func.now())
	title = Column(String, nullable=False)
	description = Column(String, nullable=True)
