"""
Scanner engine.
"""

from app.services.indicator_engine import IndicatorEngine


class ScannerEngine:
    """
    Main scanner.
    """

    def __init__(self):
        self.indicators = IndicatorEngine()