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
            candles['candles'] = pd.DataFrame(candles['candles'])
            candles['candles']['open']  = candles['candles']['mid'].map(lambda x: x['o']).astype(float)
            candles['candles']['high']  = candles['candles']['mid'].map(lambda x: x['h']).astype(float)
            candles['candles']['low']   = candles['candles']['mid'].map(lambda x: x['l']).astype(float)
            candles['candles']['close'] = candles['candles']['mid'].map(lambda x: x['c']).astype(float)
            candles['candles']['time'] = pd.to_datetime(candles['candles']['time'], unit='s')
            del candles['candles']['mid']
            return candles
        return response.raise_for_status()

    @classmethod
    def get_orderbook(cls, instrument_name, time=None):
        url = f"{cls._config['base_url']}/v3/instruments/{instrument_name}/orderBook"
        response = RequestSender.send(url, cls._headers, RequestType.GET, params={"time": time})

        if response.status_code == 200:
            orderbook = response.json()['orderBook']
            # orderbook['time'] is UTC time, so it is consistent with the time given in the candles
            # there is also orderbook['unixTime'], but it seems like it's Singapore time UTC+8
            orderbook['time'] = datetime.fromisoformat(orderbook['time'][:-1])
            orderbook['price'] = float(orderbook['price'])
            orderbook['bucketWidth'] = float(orderbook['bucketWidth'])
            orderbook['buckets'] = pd.DataFrame(orderbook['buckets']).astype(float)
            return orderbook
        return response.raise_for_status()

    @classmethod
    def get_positionbook(cls, instrument_name, time=None):
        url = f"{cls._config['base_url']}/v3/instruments/{instrument_name}/positionBook"
        response = RequestSender.send(url, cls._headers, RequestType.GET, params={"time": time})

        if response.status_code == 200:
            positionbook = response.json()['positionBook']
            positionbook['time'] = datetime.fromisoformat(positionbook['time'][:-1])
            positionbook['price'] = float(positionbook['price'])
            positionbook['bucketWidth'] = float(positionbook['bucketWidth'])
            positionbook['buckets'] = pd.DataFrame(positionbook['buckets']).astype(float)
            return positionbook
        return response.raise_for_status()