import talib
import pandas as pd

from catalyst import run_algorithm
from catalyst.api import symbol


def initialize(context):
    print('initializing')
    context.asset = symbol('eth_btc')


def handle_data(context, data):
    print('handling bar: {}'.format(data.current_dt))

    price = data.current(context.asset, 'close')
    print('got price {price}'.format(price=price))

    # prices = data.history(
    #     context.asset,
    #     fields='price',
    #     bar_count=20,
    #     frequency='1T'
    # )
    # rsi = talib.RSI(prices.values, timeperiod=14)[-1]
    # print('got rsi: {}'.format(rsi))
    pass


run_algorithm(
    capital_base=250,
    start=pd.to_datetime('2017-1-1', utc=True),
    end=pd.to_datetime('2017-10-22', utc=True),
    data_frequency='daily',
    initialize=initialize,
    handle_data=handle_data,
    analyze=None,
    exchange_name='poloniex',
    algo_namespace='simple_loop',
    base_currency='btc'
)
# run_algorithm(
#     initialize=initialize,
#     handle_data=handle_data,
#     analyze=None,
#     exchange_name='bittrex',
#     live=True,
#     algo_namespace='simple_loop',
#     base_currency='eth',
#     live_graph=False
# )
