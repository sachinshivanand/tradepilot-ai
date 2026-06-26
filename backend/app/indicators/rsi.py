"""
Relative Strength Index (RSI) using Wilder's smoothing.
"""

def rsi(values: list[float], period: int = 14) -> list[float | None]:
    """
    Calculate RSI using Wilder's smoothing method.
    """

    if period <= 0:
        raise ValueError("period must be greater than zero")

    if len(values) <= period:
        return [None] * len(values)

    result: list[float | None] = [None] * len(values)

    gains: list[float] = []
    losses: list[float] = []

    # Initial gains/losses
    for i in range(1, period + 1):
        delta = values[i] - values[i - 1]

        gains.append(max(delta, 0.0))
        losses.append(max(-delta, 0.0))

    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period

    if avg_loss == 0:
        result[period] = 100.0
    else:
        rs = avg_gain / avg_loss
        result[period] = 100 - (100 / (1 + rs))

    # Wilder smoothing
    for i in range(period + 1, len(values)):
        delta = values[i] - values[i - 1]

        gain = max(delta, 0.0)
        loss = max(-delta, 0.0)

        avg_gain = ((avg_gain * (period - 1)) + gain) / period
        avg_loss = ((avg_loss * (period - 1)) + loss) / period

        if avg_loss == 0:
            result[i] = 100.0
        else:
            rs = avg_gain / avg_loss
            result[i] = 100 - (100 / (1 + rs))

    return result