import pytest

from app.indicators.ema import ema


def test_empty():
    assert ema([], 5) == []


def test_invalid_period():
    with pytest.raises(ValueError):
        ema([1, 2, 3], 0)


def test_short_input():
    assert ema([1, 2], 5) == [None, None]


def test_period_3():
    values = [1, 2, 3, 4, 5]

    result = ema(values, 3)

    assert result[0] is None
    assert result[1] is None

    assert result[2] == 2.0

    assert round(result[3], 2) == 3.0
    assert round(result[4], 2) == 4.0