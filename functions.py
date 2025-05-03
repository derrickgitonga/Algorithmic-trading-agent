import numpy as np
def trade(resistance_levels, support_levels, hist):
    print("running trade function")
    resistance_levels = np.array(resistance_levels)
    support_levels = np.array(support_levels)
    levels = np.concatenate((resistance_levels, support_levels))
    print(levels)
    i=-95
    high = hist.High.iloc[i]
    low = hist.Low.iloc[i]
    print(f"levles are {high}, {low}")
    for level in levels:
        if abs(high - level) < 0.0007 or abs(low - level) < 0.0007:
            print(f"pin bar close to level: {level}")
            return level
        else:
            print(f"pin bar far from level: {level}")
        '''if bearish == 1:
            if closed > opened:
                check = closed
            else:
                check = opened
            if check > level:
                if check - level > 0.0007:
                    print("pin bar too far")
                else:
                    print("pin bar close to level" + level)
                    return level
            else:
                if level - check > 0.0005:
                    print(f"distance is {level-check}")
                    print("pin bar too far")
                else:
                    print("pin bar close to level" + level)
                    return level
        elif bearish == 0:
            if closed > opened:
                check = opened
            else:
                check = closed
            if check > level:
                if check - level > 0.0005:
                    print("pin bar too far")
                else:
                    print("pin bar close to level" + level)
                    return level
            else:
                if level - check > 0.0007:
                    print("pin bar too far")
                else:
                    print("pin bar close to level" + level)
                    return level
    else:
        return 0'''


""" def green(hist, light, bearish):
    i = -2
    bar0 = [hist.High.iloc[i-2],hist.Low.iloc[i-2], hist.Open.iloc[i-2], hist.Close.iloc[i-2]]
    bar1 = [hist.High.iloc[i-3],hist.Low.iloc[i-3], hist.Open.iloc[i-3], hist.Close.iloc[i-3]]
    bar2 = [hist.High.iloc[i-4],hist.Low.iloc[i-4], hist.Open.iloc[i-4], hist.Close.iloc[i-4]]
    bar3 = [hist.High.iloc[i-5],hist.Low.iloc[i-5], hist.Open.iloc[i-5], hist.Close.iloc[i-5]]
    bararray = [bar0, bar1, bar2, bar3]
    if light is None or light == 0:
        print('market not on level')
        return [0, ""]
    else:
        if bearish == 0:
            for bar in bararray:
                if bar[2] > bar[3]:
                    higher = bar[2]
                else:
                    higher = bar[3]
                if bar[1] <= light:
                    print("too many touches")
                    return [1, "cautious buy"]
                elif higher - light >= 0.0019:
                    print(light)
                    print('Possible Buy')
                    return [1, "Buy"]
        elif bearish == 1:
            for bar in bararray:
                if bar[2] > bar[3]:
                    lower = bar[3]
                else:
                    lower = bar[2]
                if bar[0] >= light:
                    print("too many touches")
                    return [1, "Cautious sell"]
                elif light - lower >= 0.0019:
                    print("Possible Sell")
                    return [1, "Sell"]
        print('not 20 pips high') """