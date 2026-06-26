"""
Utility functions for technical indicators.
"""

from app.schemas.market import Candle


def closes(candles: list[Candle]) -> list[float]:
    """Extract closing prices."""
    return [c.close for c in candles]


def opens(candles: list[Candle]) -> list[float]:
    """Extract opening prices."""
    return [c.open for c in candles]


def highs(candles: list[Candle]) -> list[float]:
    """Extract high prices."""
    return [c.high for c in candles]


def lows(candles: list[Candle]) -> list[float]:
    """Extract low prices."""
    return [c.low for c in candles]


def volumes(candles: list[Candle]) -> list[int]:
    """Extract volumes."""
    return [c.volume for c in candles]