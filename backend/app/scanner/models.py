"""
Scanner result models.
"""

from pydantic import BaseModel


class ScanResult(BaseModel):
    """
    Result returned by the scanner.
    """

    symbol: str

    score: int

    passed: bool

    trend: str

    ema20: float | None
    ema50: float | None
    ema200: float | None

    rsi: float | None

    reasons: list[str]