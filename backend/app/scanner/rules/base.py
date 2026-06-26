"""
Scanner rule interface.
"""

from abc import ABC, abstractmethod

from app.scanner.models import ScanResult


class ScannerRule(ABC):
    """
    Base class for all scanner rules.
    """

    @abstractmethod
    def evaluate(
        self,
        result: ScanResult,
    ) -> None:
        """
        Evaluate and modify the scan result.
        """
        raise NotImplementedError