from poandy.util.request import RequestSender, RequestType
from poandy.controller.base import Controller

import pandas as pd
from datetime import datetime

class InstrumentController(Controller):
    @classmethod
    def get_candles(cls, instrument_name, candle_params={}):
        url = f"{cls._config['base_url']}/v3/instruments/{instrument_name}/candles"
        response = RequestSender.send(url, cls._headers, RequestType.GET, params=candle_params)
        if response.status_code == 200:
            candles = response.json()
            candles = pd.DataFrame(candles['candles'])
            candles['open']  = candles['mid'].map(lambda x: x['o']).astype(float)
            candles['high']  = candles['mid'].map(lambda x: x['h']).astype(float)
            candles['low']   = candles['mid'].map(lambda x: x['l']).astype(float)
            candles['close'] = candles['mid'].map(lambda x: x['c']).astype(float)
            candles['time'] = pd.to_datetime(candles['time'], unit='s')
            del candles['mid']
            return candles
        return response.raise_for_status()

    @classmethod
    def get_orderbook(cls, instrument_name, datetime=None):
        url = f"{cls._config['base_url']}/v3/instruments/{instrument_name}/orderBook"
        response = RequestSender.send(url, cls._headers, RequestType.GET, params={"time": datetime})
        if response.status_code == 200:
            orderbook = response.json()['orderBook']
            orderbook['buckets'] = pd.DataFrame(orderbook['buckets']).astype(float)
            return orderbook
        return response.raise_for_status()

    @classmethod
    def get_positionbook(cls, instrument_name, datetime=None):
        url = f"{cls._config['base_url']}/v3/instruments/{instrument_name}/positionBook"
        response = RequestSender.send(url, cls._headers, RequestType.GET, params={"time": datetime})
        if response.status_code == 200:
            positionbook = response.json()['positionBook']
            positionbook['buckets'] = pd.DataFrame(positionbook['buckets']).astype(float)
            return positionbook
        return response.raise_for_status()