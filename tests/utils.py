import os
from pathlib import Path

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.app import App
from app.database.db_admin import Base, get_db

# Test environment SQLite database
DB_PATH = "./test.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

# SQLAlchemy engine and session for the test db
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def spin_up():
    """
    Create the test environment by:
            1. Creating the test database and tables
            2. Overriding the app dependency get_db with a version
            using the local testing session
            3. Create the test client
    """
    tear_down()

    app = App()

    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)

    return client


def tear_down():
    """
    Tear down the test environment, deleting the test database
    SQLite file.
    """
    if Path(DB_PATH).is_file():
        os.remove(DB_PATH)
