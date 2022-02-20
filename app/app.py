from fastapi import FastAPI

from app.database import models, database
from app.resources import router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(router)