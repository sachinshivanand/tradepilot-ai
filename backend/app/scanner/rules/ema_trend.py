"""
EMA Trend Rule.
"""

from app.scanner.models import ScanResult
from app.scanner.rules.base import ScannerRule
from app.scanner.scoring import EMA_ALIGNMENT_SCORE


class EMATrendRule(ScannerRule):
    """
    Bullish trend if EMA20 > EMA50 > EMA200.
    """

    def evaluate(self, result: ScanResult) -> None:
        if (
            result.ema20 is None
            or result.ema50 is None
            or result.ema200 is None
        ):
            return

        if result.ema20 > result.ema50 > result.ema200:
            result.score += EMA_ALIGNMENT_SCORE
            result.trend = "BULLISH"
            result.reasons.append(
                "EMA20 > EMA50 > EMA200"
            )