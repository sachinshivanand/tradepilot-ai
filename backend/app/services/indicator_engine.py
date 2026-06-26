"""
Technical Indicator Engine.
"""

from app.indicators import ema, rsi, sma
from app.indicators.utils import closes
from app.schemas.market import Candle


class IndicatorEngine:
    """
    Computes technical indicators from market data.
    """

    def sma(
        self,
        candles: list[Candle],
        period: int,
    ) -> list[float | None]:
        return sma(closes(candles), period)

    def ema(
        self,
        candles: list[Candle],
        period: int,
    ) -> list[float | None]:
        return ema(closes(candles), period)
    
    def rsi(
        self,
        candles: list[Candle],
        period: int = 14,
    ) -> list[float | None]:
        return rsi(closes(candles), period)