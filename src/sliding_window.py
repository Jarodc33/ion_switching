import numpy as np
import pandas as pd


def make_sliding_window(array, window_size, offset = 0):
    """
    offset = number of zeros added to the begining 
    """
    array = np.append(np.append(np.zeros(offset), array), np.zeros(window_size - offset))
    sliding_window_array = [array[0: -window_size]]
    for i in range(1, window_size):
        sliding_window_array = np.append(sliding_window_array, [array[i:i - window_size]], axis = 0)
    return sliding_window_array.T


def make_sliding_window_series(series, window_size):
    col_names = [series.name + str(i) for i in range(window_size)]
    return pd.DataFrame(make_sliding_window(series, window_size, window_size // 2), columns = col_names)


def make_sliding_window_frame(data, window_size):
    sliding_window = make_sliding_window_series(data['signal'], window_size)
    sliding_window['open_channels'] = data['open_channels'].reset_index(drop = True)
    return sliding_window