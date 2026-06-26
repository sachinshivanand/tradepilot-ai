from datetime import datetime

from app.providers.market.mock import MockMarketDataProvider
from app.services.indicator_engine import IndicatorEngine


def test_sma():
    provider = MockMarketDataProvider()

    candles = provider.get_history(
        symbol="BEL",
        start=datetime(2026, 1, 1),
        end=datetime(2026, 1, 10),
    )

    engine = IndicatorEngine()

    result = engine.sma(candles, 3)

    assert result[0] is None
    assert result[2] == 102.0


def test_ema():
    provider = MockMarketDataProvider()

    candles = provider.get_history(
        symbol="BEL",
        start=datetime(2026, 1, 1),
        end=datetime(2026, 1, 10),
    )

    engine = IndicatorEngine()

    result = engine.ema(candles, 3)

    assert result[0] is None
    assert result[2] == 102.0