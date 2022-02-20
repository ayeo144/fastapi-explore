from typing import Optional

from pydantic import BaseModel


class EntryBase(BaseModel):
    title: str
    description: Optional[str] = None


class EntryCreate(EntryBase):
    pass


class Entry(EntryBase):
    id: int

    class Config:
        """
        Assign configuration to pydantic models.
        """

        orm_mode = True
