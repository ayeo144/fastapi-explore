from fastapi import Depends, HTTPException, APIRouter
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session

from app.database import crud, db_admin, schemas


ENDPOINT = "entry"
entry_router = APIRouter()


@cbv(entry_router)
class Entry:
    """
    Requests for the "entry" endpoint.
    """

    @entry_router.post(f"/{ENDPOINT}", response_model=schemas.Entry)
    def create_entry(
        self, entry: schemas.EntryCreate, db: Session = Depends(db_admin.get_db)
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

    @entry_router.get(f"/{ENDPOINT}/{{title}}", response_model=schemas.Entry)
    def get_entry(self, title: str, db: Session = Depends(db_admin.get_db)):
        """
        Get entry with specific title.
        """
        entry = crud.get_entry_by_title(db, title)
        if entry is None:
            raise HTTPException(
                status_code=400, detail="Entry with title does not exist"
            )
        return entry
