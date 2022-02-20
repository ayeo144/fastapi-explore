from sqlalchemy.orm import Session

from app.database import models, schemas


def create_entry(db: Session, entry: schemas.EntryCreate):
    """
    Add a new entry to the database.

    :param db: the sqlalchemy Session object
    :param entry: the entry object defined by the EntryCreate schema
    """
    new_entry = models.Entry(**entry.dict())
    db.add(new_entry)
    db.commit()
    return new_entry


def get_entry_by_title(db: Session, title: str):
    return db.query(models.Entry).filter_by(title=title).all()


def get_entries(db: Session):
    return db.query(models.Entry).all()


def update_entry(self):
    ...


def delete_entry(self):
    ...
