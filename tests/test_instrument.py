import pytest
import pandas as pd

from poandy.controller.instrument import InstrumentController


class TestInstrumentController:
    def test_get_candles(self):
        candles = InstrumentController.get_candles('USD_CAD')
        assert 'instrument' in candles
        assert 'granularity' in candles
        assert 'candles' in candles
        assert isinstance(candles['candles'], pd.DataFrame)
        
    def test_get_orderbook(self):
        orderbook = InstrumentController.get_orderbook('USD_CAD')
        assert 'instrument' in orderbook
        assert 'time' in orderbook
        assert 'price' in orderbook
        assert 'bucketWidth' in orderbook
        assert 'buckets' in orderbook
        assert isinstance(orderbook['buckets'], pd.DataFrame)

    def test_get_positionbook(self):
        positionbook = InstrumentController.get_positionbook('USD_CAD')
        assert 'instrument' in positionbook
        assert 'time' in positionbook
        assert 'price' in positionbook
        assert 'bucketWidth' in positionbook
        assert 'buckets' in positionbook
        assert isinstance(positionbook['buckets'], pd.DataFrame)