"""
Health check endpoint.
"""

from fastapi import APIRouter

router = APIRouter()
router = APIRouter(tags=["System"])

@router.get("/health")
async def health():
    """
    Health check endpoint.
    """
    return {
        "success": True,
        "data": {
            "status": "healthy",
        },
    }