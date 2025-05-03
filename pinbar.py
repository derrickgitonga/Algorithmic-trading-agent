def pinbar(df):
    i=-95
    df.columns = df.columns.get_level_values(0)
    print(df)
    high = df.High.iloc[i]
    low = df.Low.iloc[i]
    opened = df.Open.iloc[i]
    closed = df.Close.iloc[i]
    height = high - low
    print(f"closed is {closed}")
    body = closed - opened
    body = abs(body)
    if height < 0.0009:
        return [0, 0]
    else:
        #create an empty array 
        result = []
        #call the direction funtion
        result = direction(closed, opened, high, low)
        wick = result[0]
        wick_body_ratio = wick / body
        wick_body_ratio = abs(wick_body_ratio)
        if wick_body_ratio > 0.9:
            print("pinbar present")
            #return bias and pin bar present
            return [result[1], 1]
        else:
            print("pinbar is not present")
            #return the bias and pin ba not present
            return [result[1], 0]


def direction(closed, opened, high, low):
    #declare wick as zero
    wick = 0
    #declare a global variable bearish
    global bearish
    if closed > opened:
        upper_wick = high - closed
        lower_wick = opened - low
    else:
        upper_wick = high - opened
        lower_wick = closed - low
    if upper_wick > lower_wick:
        bearish = 1
        if lower_wick != 0:
            wick_ratio = upper_wick / lower_wick
            if wick_ratio >= 1.5:
                wick = upper_wick
        else:
            wick = upper_wick
    elif lower_wick > upper_wick:
        bearish = 0
        if upper_wick != 0:
            wick_ratio = lower_wick / upper_wick
            if wick_ratio >= 1.5:
                wick = lower_wick
        else:
            wick = lower_wick
    #return the length of the wick as wick and the direction as berish (either bullish or bearish)
    return [wick, bearish]
