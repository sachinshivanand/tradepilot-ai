from datetime import datetime

from app.indicators.utils import closes, highs, lows, opens, volumes
from app.schemas.market import Candle


def sample_candles():
    return [
        Candle(
            symbol="BEL",
            timestamp=datetime(2026, 1, 1),
            open=100,
            high=105,
            low=99,
            close=104,
            volume=1000,
        ),
        Candle(
            symbol="BEL",
            timestamp=datetime(2026, 1, 2),
            open=104,
            high=108,
            low=103,
            close=107,
            volume=1200,
        ),
    ]


def test_closes():
    assert closes(sample_candles()) == [104, 107]


def test_opens():
    assert opens(sample_candles()) == [100, 104]


def test_highs():
    assert highs(sample_candles()) == [105, 108]


def test_lows():
    assert lows(sample_candles()) == [99, 103]


def test_volumes():
    assert volumes(sample_candles()) == [1000, 1200]