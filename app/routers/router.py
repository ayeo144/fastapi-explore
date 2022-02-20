"""
Create the main APIRouter object including routers from all
the specific endpoints.
"""

from fastapi_utils.inferring_router import InferringRouter
from fastapi import APIRouter

from app.routers.entry import entry_router
from app.routers.entries import entries_router

api_router = APIRouter()
api_router.include_router(entry_router)
api_router.include_router(entries_router)