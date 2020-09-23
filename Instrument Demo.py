# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from poandy.controller.instrument import InstrumentController
from poandy.controller.account import AccountController

import pandas as pd


# %%
account_id = AccountController.get_default_account_id()


# %%
instruments = AccountController.get_tradeable_instruments(account_id, names_only=True)
pairs = list(map(lambda x: x.split('_'), instruments))
currency1 = [x[0] for x in pairs]
currency2 = [x[1] for x in pairs]
instruments = pd.DataFrame({'currency1': currency1, 'currency2': currency2, 'instrument': instruments})
instruments


# %%
instruments[instruments['currency1'] == 'USD']


# %%
candles = InstrumentController.get_candles("USD_CAD")
candles


# %%
import plotly.graph_objects as go

candles_data = go.Candlestick(
    x=candles['time'],
    open=candles['open'],
    high=candles['high'],
    low=candles['low'],
    close=candles['close'])
fig = go.Figure(data=[candles_data])

fig.show()


# %%
orderbook = InstrumentController.get_orderbook("USD_CAD")
orderbook


# %%
print(orderbook['buckets'].dtypes)
orderbook['buckets']


# %%
positionbook = InstrumentController.get_positionbook("USD_CAD")
positionbook
# "The snapshot for USD_CAD does not exist at the given time 2020-09-23T16:20:00Z." → handle this gracefully


# %%
print(positionbook['buckets'].dtypes)
positionbook['buckets']


# %%



