import MetaTrader5 as mt5
import pandas as pd
def execute_trade(bearish, entry_price = 0):
    print("executing trade")
    if not mt5.initialize(login=907473, server="EGMSecurities-Demo",password="Gods_kid57"):
        print("initialize() failed, error code =",mt5.last_error())
        return False
    # display data on connection status, server name and trading account
    print(mt5.terminal_info())
    tick = mt5.symbol_info_tick("EURUSD")
    if tick is None:
        print("Failed to get tick data")
        return False
    current_price = tick.ask if bearish == 0 else tick.bid
    entry = entry_price if entry_price is not None else current_price
    pip = 0.0001
    stop_loss =  entry + 10 * pip if bearish == 1 else entry - 10 * pip
    take_price = entry + 20 * pip if bearish == 0 else entry - 20 * pip

    order_type = mt5.ORDER_TYPE_BUY if bearish == 0 else mt5.ORDER_TYPE_SELL
    price = tick.ask if bearish == 0 else tick.bid

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": 'EURUSD',
        "volume": 0.01,
        "type": order_type,
        "price": price,
        "sl": stop_loss,
        "tp": take_price,
        "deviation": 5,
        "type_filling": mt5.ORDER_FILLING_IOC,
        "comment": "Quantra Market Buy Order",
    }
    order_result = mt5.order_send(request)
    if order_result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Error placing order: {order_result.retcode} - {order_result.comment}")
        return False
    else:
        print(f"Order placed successfully: {'sell' if bearish else 'buy'} at {price} , order ticket:", order_result.order)