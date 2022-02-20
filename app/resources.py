from typing import List

from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

from app.database import crud, database, schemas

router = InferringRouter()


@cbv(router)
class Entry:
    """
    Endpoints for working with single Entry.
    """

    @router.post("/entry", response_model=schemas.Entry)
    def create_entry(
        self, entry: schemas.EntryCreate, db: Session = Depends(database.get_db)
    ):
        """
        Create a new entry.
        """
        entry_check = crud.get_entry_by_title(db, entry.title)
        if entry_check is not None:
            raise HTTPException(
                status_code=400, detail="Entry with title already exists"
            )
        else:
            entry = crud.create_entry(db, entry)
        return entry

    @router.get("/entry/{title}", response_model=schemas.Entry)
    def get_entry(self, title: str, db: Session = Depends(database.get_db)):
        """
        Get entry with specific title.
        """
        entry = crud.get_entry_by_title(db, title)
        if entry is None:
            raise HTTPException(
                status_code=400, detail="Entry with title does not exist"
            ) 
        return entry           


@cbv(router)
class Entries:
    """
    Endpoints for working with multipl Entries.
    """

    @router.get("/entries", response_model=List[schemas.Entry])
    def get_entries(self, db: Session = Depends(database.get_db)):
        """
        Get all entries in database.
        """
        return crud.get_entries(db)
