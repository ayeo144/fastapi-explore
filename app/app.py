from fastapi import FastAPI

from app.database import db_admin, models
from app.routers import api_router


class App(FastAPI):
    """
    Main application, inherits from the fastapi.FastAPI
    class allowing us to control the flow of events when
    setting up the API, such as when the database is created.
    """

    def __init__(self):
        """
        Initialise the class and add the router containing the
        endpoints.
        """
        super().__init__()
        self.include_router(api_router)

    def create_db(self):
        """
        Create the SQLite database and tables.
        """
        models.Base.metadata.create_all(bind=db_admin.engine)
