"""
Root API endpoint.
"""

from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()
router = APIRouter(tags=["System"])

@router.get("/")
async def root():
    """
    Root endpoint.
    """
    return {
        "success": True,
        "data": {
            "application": settings.app_name,
            "version": settings.app_version,
            "status": "running",
        },
    }