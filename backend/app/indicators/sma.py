"""
Simple Moving Average (SMA).
"""

import numpy as np


def sma(values: list[float], period: int) -> list[float | None]:
    """
    Calculate Simple Moving Average.

    Returns a list of the same length as the input.
    Values before enough data is available are None.
    """

    if period <= 0:
        raise ValueError("period must be greater than zero")

    if len(values) == 0:
        return []

    result: list[float | None] = []

    for i in range(len(values)):
        if i + 1 < period:
            result.append(None)
            continue

        window = values[i + 1 - period : i + 1]
        result.append(float(np.mean(window)))

    return result