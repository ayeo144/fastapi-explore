from fastapi import FastAPI

from app.database import database, models
from app.resources import router


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
        self.include_router(router)

    def create_db(self):
        """
        Create the SQLite database and tables.
        """
        models.Base.metadata.create_all(bind=database.engine)
