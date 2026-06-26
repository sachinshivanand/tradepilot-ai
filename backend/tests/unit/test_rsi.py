import pytest

from app.indicators.rsi import rsi


def test_empty():
    assert rsi([], 14) == []


def test_invalid_period():
    with pytest.raises(ValueError):
        rsi([1, 2, 3], 0)


def test_short_input():
    assert rsi([1, 2, 3], 14) == [None, None, None]


def test_uptrend_reaches_high_rsi():
    prices = list(range(1, 31))

    values = rsi(prices, 14)

    assert values[-1] is not None
    assert values[-1] > 90