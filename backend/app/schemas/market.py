"""
Pydantic schemas for market data.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class Symbol(BaseModel):
    """Market symbol."""

    symbol: str = Field(..., examples=["BEL"])
    name: str = Field(..., examples=["Bharat Electronics Ltd"])
    exchange: str = Field(default="NSE")


class Quote(BaseModel):
    """Real-time market quote."""

    symbol: str

    last_price: float
    change: float
    change_percent: float

    volume: int

    timestamp: datetime


class Candle(BaseModel):
    """OHLCV candle."""

    symbol: str

    timestamp: datetime

    open: float
    high: float
    low: float
    close: float

    volume: int


class ScanCandidate(BaseModel):
    """Scanner output candidate."""

    symbol: str

    score: float = Field(ge=0, le=100)
    confidence: float = Field(ge=0, le=100)

    reason: str