import numpy as np
from scipy.stats import linregress
def calculate_support_resistance(df):
    print("calculating SR")
    df = df[['High', 'Low']]
    df.columns = df.columns.get_level_values(1)
    df.columns = ['High', 'Low']
    dataset_length = len(df)
    
    index = 0
    chunk_count = 0
    max_highs = []
    min_lows = []
    
    resistance_levels = []
    support_levels = []
    
    while index < dataset_length:
        # Extract 20 candles
        chunk = df.iloc[index:index + 20]
        
        if not chunk.empty:
            max_highs.append(chunk["High"].max())  # Store max high
            min_lows.append(chunk["Low"].min())  # Store min low
        
        chunk_count += 1
        index += 20  # Move to the next 20 candles

        # Once we process 5 chunks, fit best-fit lines
        if chunk_count == 5:
            # Remove outliers
            max_highs_filtered = remove_outliers(max_highs)
            min_lows_filtered = remove_outliers(min_lows)

            # Fit best-fit lines
            resistance_line = fit_horizontal_line(max_highs_filtered)
            support_line = fit_horizontal_line(min_lows_filtered)


            if resistance_line:
                resistance_levels.append(resistance_line)
            if support_line:
                support_levels.append(support_line)

            # Reset for next batch
            chunk_count = 0
            max_highs = []
            min_lows = []
    
    return resistance_levels, support_levels


def fit_horizontal_line(values):
    if len(values) == 0:
        return None
    else:
        return float(np.mean(values))



def remove_outliers(values, pip_size=0.0004):
    mean = np.mean(values)
    return [v for v in values if abs(v - mean) <= (4 * pip_size)]
