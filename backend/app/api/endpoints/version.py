"""
Application version endpoint.
"""

from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()
router = APIRouter(tags=["System"])

@router.get("/version")
async def version():
    """
    Return application version.
    """
    return {
        "success": True,
        "data": {
            "application": settings.app_name,
            "version": settings.app_version,
        },
    }