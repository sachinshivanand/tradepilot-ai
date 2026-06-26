"""
Mock implementation of a market data provider.
"""

from datetime import datetime, timedelta

from app.providers.market.base import MarketDataProvider
from app.schemas.market import Candle, Quote, Symbol


class MockMarketDataProvider(MarketDataProvider):
    """Mock provider for local development and testing."""

    def get_quote(self, symbol: str) -> Quote:
        return Quote(
            symbol=symbol,
            last_price=350.25,
            change=5.10,
            change_percent=1.48,
            volume=1_250_000,
            timestamp=datetime.now(),
        )

    def get_history(
        self,
        symbol: str,
        start: datetime,
        end: datetime,
        interval: str = "1d",
    ) -> list[Candle]:
        candles: list[Candle] = []

        current = start
        price = 100.0

        while current <= end:
            candles.append(
                Candle(
                    symbol=symbol,
                    timestamp=current,
                    open=price,
                    high=price + 2,
                    low=price - 2,
                    close=price + 1,
                    volume=1_000_000,
                )
            )

            current += timedelta(days=1)
            price += 1

        return candles

    def get_symbols(self) -> list[Symbol]:
        return [
            Symbol(
                symbol="BEL",
                name="Bharat Electronics Ltd",
                exchange="NSE",
            ),
            Symbol(
                symbol="ICICIBANK",
                name="ICICI Bank Ltd",
                exchange="NSE",
            ),
            Symbol(
                symbol="CGPOWER",
                name="CG Power & Industrial Solutions",
                exchange="NSE",
            ),
        ]

    def get_top_volume(self) -> list[Quote]:
        return [
            self.get_quote("BEL"),
            self.get_quote("ICICIBANK"),
            self.get_quote("CGPOWER"),
        ]

    def get_top_value(self) -> list[Quote]:
        return self.get_top_volume()