from typing import List

from fastapi import Depends, HTTPException, APIRouter
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session

from app.database import crud, db_admin, schemas


ENDPOINT = "entries"
entries_router = APIRouter()


@cbv(entries_router)
class Entries:
    """
    Endpoints for working with multipl Entries.
    """

    @entries_router.get(f"/{ENDPOINT}", response_model=List[schemas.Entry])
    def get_entries(self, db: Session = Depends(db_admin.get_db)):
        """
        Get all entries in database.
        """
        return crud.get_entries(db)