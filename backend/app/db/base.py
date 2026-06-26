"""
Base class for all SQLAlchemy ORM models.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all ORM models."""

    pass


# Import all ORM models here so Alembic can discover them.
import app.models  # noqa: E402,F401