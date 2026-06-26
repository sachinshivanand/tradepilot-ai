from app.scanner.models import ScanResult
from app.scanner.rules.rsi import RSIRule


def test_rsi_in_range():
    result = ScanResult(
        symbol="BEL",
        score=0,
        passed=False,
        trend="NEUTRAL",
        ema20=None,
        ema50=None,
        ema200=None,
        rsi=62,
        reasons=[],
    )

    RSIRule().evaluate(result)

    assert result.score == 30
    assert len(result.reasons) == 1


def test_rsi_out_of_range():
    result = ScanResult(
        symbol="BEL",
        score=0,
        passed=False,
        trend="NEUTRAL",
        ema20=None,
        ema50=None,
        ema200=None,
        rsi=82,
        reasons=[],
    )

    RSIRule().evaluate(result)

    assert result.score == 0