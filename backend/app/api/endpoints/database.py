"""
Database health endpoint.
"""

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter(
    prefix="/database",
    tags=["Database"],
)


@router.get("/health")
async def database_health(db: Session = Depends(get_db)):
    """
    Verify database connectivity.
    """
    db.execute(text("SELECT 1"))

    return {
        "success": True,
        "data": {
            "database": "connected",
        },
    }