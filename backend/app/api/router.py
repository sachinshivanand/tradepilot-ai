"""
Central API router.
"""

from fastapi import APIRouter

from app.api.endpoints import database, health, root, version

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(root.router)
api_router.include_router(health.router)
api_router.include_router(version.router)
api_router.include_router(database.router)