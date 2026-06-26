"""
Base interface for market data providers.
"""

from abc import ABC, abstractmethod
from datetime import datetime

from app.schemas.market import Candle, Quote, Symbol


class MarketDataProvider(ABC):
    """
    Abstract base class for market data providers.
    """

    @abstractmethod
    def get_quote(self, symbol: str) -> Quote:
        """
        Return the latest quote for a symbol.
        """
        raise NotImplementedError

    @abstractmethod
    def get_history(
        self,
        *,
        symbol: str,
        start: datetime,
        end: datetime,
        interval: str = "1d",
    ) -> list[Candle]:
        """
        Return historical OHLCV data.
        """
        raise NotImplementedError

    @abstractmethod
    def get_symbols(self) -> list[Symbol]:
        """
        Return the list of supported symbols.
        """
        raise NotImplementedError

    @abstractmethod
    def get_top_volume(self) -> list[Quote]:
        """
        Return today's top volume stocks.
        """
        raise NotImplementedError

    @abstractmethod
    def get_top_value(self) -> list[Quote]:
        """
        Return today's top traded value stocks.
        """
        raise NotImplementedError