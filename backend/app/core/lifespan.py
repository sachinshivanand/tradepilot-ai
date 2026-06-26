from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import configure_logging, get_logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    logger = get_logger(__name__)

    logger.info("=" * 60)
    logger.info("%s v%s", settings.app_name, settings.app_version)
    logger.info("Application startup")
    logger.info("Debug mode: %s", settings.debug)
    logger.info("Database: %s", settings.database_url)
    logger.info("=" * 60)

    yield

    logger.info("Application shutdown")
    