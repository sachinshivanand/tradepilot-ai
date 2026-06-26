"""
Scanner engine.
"""
from datetime import datetime, timedelta

from app.providers.market.factory import get_market_provider
from app.scanner.models import ScanResult
from app.scanner.rules.ema_trend import EMATrendRule
from app.scanner.rules.rsi import RSIRule
from app.services.indicator_engine import IndicatorEngine


class ScannerEngine:
    """
    Executes scanner rules on a symbol.
    """

    def __init__(self):
        self.provider = get_market_provider()
        self.indicators = IndicatorEngine()

        self.rules = [
            EMATrendRule(),
            RSIRule(),
        ]

    def scan_symbol(self, symbol: str) -> ScanResult:
        """
        Scan a single symbol.
        """
        end = datetime.now()
        start = end - timedelta(days=365)

        candles = self.provider.get_history(
            symbol=symbol,
            start=start,
            end=end,
        )

        ema20 = self.indicators.ema(candles, 20)
        ema50 = self.indicators.ema(candles, 50)
        ema200 = self.indicators.ema(candles, 200)
        rsi14 = self.indicators.rsi(candles)

        result = ScanResult(
            symbol=symbol,
            score=0,
            passed=False,
            trend="NEUTRAL",
            ema20=ema20[-1],
            ema50=ema50[-1],
            ema200=ema200[-1],
            rsi=rsi14[-1],
            reasons=[],
        )

        for rule in self.rules:
            rule.evaluate(result)

        result.passed = result.score > 0

        return result