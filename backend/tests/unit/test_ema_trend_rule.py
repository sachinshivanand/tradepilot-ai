from app.scanner.models import ScanResult
from app.scanner.rules.ema_trend import EMATrendRule


def test_bullish_alignment():
    result = ScanResult(
        symbol="BEL",
        score=0,
        passed=False,
        trend="NEUTRAL",
        ema20=120,
        ema50=110,
        ema200=100,
        rsi=None,
        reasons=[],
    )

    EMATrendRule().evaluate(result)

    assert result.score == 40
    assert result.trend == "BULLISH"
    assert len(result.reasons) == 1


def test_non_bullish_alignment():
    result = ScanResult(
        symbol="BEL",
        score=0,
        passed=False,
        trend="NEUTRAL",
        ema20=100,
        ema50=120,
        ema200=110,
        rsi=None,
        reasons=[],
    )

    EMATrendRule().evaluate(result)

    assert result.score == 0
    assert result.trend == "NEUTRAL"