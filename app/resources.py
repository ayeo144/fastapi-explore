from typing import List

from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

from app.database import schemas, database, crud


router = InferringRouter()


@cbv(router)
class Entry:
	"""
	Endpoints for working with single Entry.
	"""

	@router.post("/entry")
	def create_entry(
		self, 
		entry: schemas.EntryCreate, 
		db: Session = Depends(database.get_db)
	):
		"""
		Create a new entry.
		"""
		entry_check = crud.get_entry_by_title(db, entry.title)
		if len(entry_check) > 0:
			raise HTTPException(status_code=400, detail="Entry with title already exists")
		return crud.create_entry(db, entry)

	@router.get("/entry/{title}")
	def get_entry(self, title: str, db: Session = Depends(database.get_db)):
		"""
		Get entry with specific title.
		"""
		return crud.get_entry_by_title(db, title)


@cbv(router)
class Entries:
	"""
	Endpoints for working with multipl Entries.
	"""

	@router.get("/entries")
	def get_entries(self, db: Session = Depends(database.get_db)):
		"""
		Get all entries in database.
		"""
		return crud.get_entries(db)
