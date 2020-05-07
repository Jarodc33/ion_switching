import numpy as np
import pandas as pd


def make_sliding_window(array, window_size, offset = 0):
    """
    Makes a sliding window from any array like structure. Each row is the original point with offset number of points before it and (windowsize - offset) number of points after it.
    
    Parameters
    ----------
    Array: the data to make the sliding window
    Window_size: new dimension of the sliding window. (1 column n length becomes a (n, window size) shape array)
    offset: the number of zeros to put before the first point. This means there is (window_size - offset) points after the last point
    
    Returns
    -------
    A sliding window array of shape (n, window_size)
    """
    array = np.append(np.append(np.zeros(offset), array), np.zeros(window_size - offset))
    sliding_window_array = [array[0: -window_size]]
    for i in range(1, window_size):
        sliding_window_array = np.append(sliding_window_array, [array[i:i - window_size]], axis = 0)
    return sliding_window_array.T


def make_sliding_window_series(series, window_size):
    """
    Makes a sliding window from a Series object. Each row is the original point with half the window size of points after and before it. The name of the series is retained
    
    Parameters
    ----------
    Array: the data to make the sliding window
    Window_size: new dimension of the sliding window. (1 column n length becomes a (n, window size) shape array)
    
    Returns
    -------
    A sliding window array of shape (n, window_size)
    """
    col_names = [series.name + str(i) for i in range(window_size)]
    return pd.DataFrame(make_sliding_window(series, window_size, window_size // 2), columns = col_names)


def make_sliding_window_frame(data, window_size):
    """
    This is the Specific implementation for this project!
    
    This will just make the code in notebooks cleaner
    """
    sliding_window = make_sliding_window_series(data['signal'], window_size)
    sliding_window['open_channels'] = data['open_channels'].reset_index(drop = True)
    return sliding_window