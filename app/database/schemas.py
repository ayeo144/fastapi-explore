from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class EntryBase(BaseModel):
    title: str
    description: Optional[str] = None


class EntryCreate(EntryBase):
    pass


class Entry(EntryBase):
    id: int
    time_created: datetime

    class Config:
        """
        Assign configuration to pydantic models.
        """

        orm_mode = True
