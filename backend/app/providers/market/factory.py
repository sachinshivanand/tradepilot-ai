"""
Factory for market data providers.
"""

from app.core.config import settings
from app.providers.market.base import MarketDataProvider
from app.providers.market.mock import MockMarketDataProvider


def get_market_provider() -> MarketDataProvider:
    """
    Return the configured market data provider.
    """

    provider = settings.market_data_provider.lower()

    if provider == "mock":
        return MockMarketDataProvider()

    raise ValueError(
        f"Unsupported market data provider: {settings.market_data_provider}"
    )