if __name__ == '__main__':
    import yfinance as yf
    import numpy as np
    import pandas as pd
    from scipy.stats import linregress
    import time as tm
    from email_send import email_send
    import schedule
    from datetime import time, datetime
    from pinbar import pinbar
    from functions import trade
    from horizontal import calculate_support_resistance
    from account import execute_trade

    #main function ro run all models
    #Returns null
    def main():
        #intialize an empty array to functions output
        d = []
        #downloading data from yahoo finance API
        ticker = "EURUSD=X"
        database = yf.download(ticker, interval="30m", period="7d")
        #call the pinbar function for pinbar reognition
        resistance_levels, support_levels = calculate_support_resistance(database)
        print(f"resistance levels, {resistance_levels}")
        print(f"support levls {support_levels}")
        d = pinbar(database)
        #If the pin bar is present
        if d[1] == 1:
            #call the trade funtion to check the distance of the pin bar from the support/resistance
            level = trade(resistance_levels, support_levels, database)
            if level:
                execute_trade(d[0], level)
        else:
            print("no opportunity")


    def trial():
        try:
            main()
        except:
            print("failed")
    schedule.every().hour.at(":30").do(trial)
    schedule.every().hour.at(":00").do(trial)
    while True:
        schedule.run_pending()
        tm.sleep(10)