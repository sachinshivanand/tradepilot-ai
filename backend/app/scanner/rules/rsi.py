"""
RSI Rule.
"""

from app.scanner.models import ScanResult
from app.scanner.rules.base import ScannerRule
from app.scanner.scoring import RSI_SCORE


class RSIRule(ScannerRule):
    """
    Score stocks whose RSI is in the bullish momentum zone.
    """

    def evaluate(self, result: ScanResult) -> None:
        if result.rsi is None:
            return

        if 55 <= result.rsi <= 70:
            result.score += RSI_SCORE
            result.reasons.append(
                "RSI in bullish momentum zone (55-70)"
            )