from app.indicators.sma import sma


def test_sma_period_3():
    result = sma([1, 2, 3, 4, 5], 3)

    assert result == [
        None,
        None,
        2.0,
        3.0,
        4.0,
    ]


def test_empty():
    assert sma([], 3) == []


def test_invalid_period():
    import pytest

    with pytest.raises(ValueError):
        sma([1, 2, 3], 0)