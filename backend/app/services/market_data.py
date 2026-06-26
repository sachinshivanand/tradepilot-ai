"""
Market data service.
"""

from datetime import datetime

from app.providers.market.factory import get_market_provider
from app.schemas.market import Candle, Quote, Symbol


class MarketDataService:
    """
    Service layer for market data.
    """

    def __init__(self) -> None:
        self.provider = get_market_provider()

    def get_quote(self, symbol: str) -> Quote:
        return self.provider.get_quote(symbol)

    def get_history(
        self,
        *,
        symbol: str,
        start: datetime,
        end: datetime,
        interval: str = "1d",
    ) -> list[Candle]:
        return self.provider.get_history(
            symbol=symbol,
            start=start,
            end=end,
            interval=interval,
        )

    def get_symbols(self) -> list[Symbol]:
        return self.provider.get_symbols()

    def get_top_volume(self) -> list[Quote]:
        return self.provider.get_top_volume()

    def get_top_value(self) -> list[Quote]:
        return self.provider.get_top_value()