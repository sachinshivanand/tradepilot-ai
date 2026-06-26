from app.scanner.models import ScanResult


def test_scan_result():
    result = ScanResult(
        symbol="BEL",
        score=0,
        passed=False,
        trend="UNKNOWN",
        ema20=None,
        ema50=None,
        ema200=None,
        rsi=None,
        reasons=[],
    )

    assert result.symbol == "BEL"