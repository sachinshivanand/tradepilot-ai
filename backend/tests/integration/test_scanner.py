from app.scanner.engine import ScannerEngine


def test_scan_symbol():
    scanner = ScannerEngine()

    result = scanner.scan_symbol("BEL")

    assert result.symbol == "BEL"