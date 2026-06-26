"""
Exponential Moving Average (EMA).
"""

from app.indicators.sma import sma


def ema(values: list[float], period: int) -> list[float | None]:
    """
    Calculate the Exponential Moving Average (EMA).

    Returns a list the same length as the input.
    Values before enough data exists are None.
    """

    if period <= 0:
        raise ValueError("period must be greater than zero")

    if not values:
        return []

    result: list[float | None] = [None] * len(values)

    if len(values) < period:
        return result

    multiplier = 2 / (period + 1)

    sma_values = sma(values, period)
    first_ema = sma_values[period - 1]

    result[period - 1] = first_ema
    previous = first_ema

    assert previous is not None

    for i in range(period, len(values)):
        current = (values[i] - previous) * multiplier + previous
        result[i] = current
        previous = current

    return result