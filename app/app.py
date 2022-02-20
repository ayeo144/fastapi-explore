from fastapi import FastAPI

from app.database import database, models
from app.resources import router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(router)
