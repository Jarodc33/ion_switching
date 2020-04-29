import numpy as np
import pandas as pd

from src.transformers import LinearTransformation, ParabolicTransformation, TrigTransformation

def chunk_data(data, number_of_chunks):
    chunks = list()
    lst = np.linspace(0, len(data), number_of_chunks + 1, dtype = int)
    for start, stop in zip(lst[0:-1], lst[1:]):
        chunks.append(data[start:stop].copy())
    return chunks

def transform_train_chunks(train_chunks):
    lt = LinearTransformation()
    tt = TrigTransformation(trig_function = 'sin')

    train_chunks[1].loc[train_chunks[1].index[:100000], 'signal'] = lt.fit_transform(train_chunks[1][:100000], 3/10, -15)
    train_chunks[6]['signal'] = tt.fit_transform(train_chunks[6].copy(), 300, 50, 4.95)
    train_chunks[7]['signal'] = tt.fit_transform(train_chunks[7].copy(), 350, 50, 5.030)
    train_chunks[8]['signal'] = tt.fit_transform(train_chunks[8].copy(), 400, 50, 4.974)
    train_chunks[9]['signal'] = tt.fit_transform(train_chunks[9].copy(), 450, 50, 5.089)
    
    return train_chunks
    
def transform_test_chunks(test_chunks):
    lt = LinearTransformation()
    tt = TrigTransformation(trig_function = 'sin')
    
    test_chunks[0]['signal'] = lt.fit_transform(test_chunks[0].copy(), 3 / 10, -150)
    test_chunks[1]['signal'] = lt.fit_transform(test_chunks[1].copy(), 3 / 10, -153)
    test_chunks[4]['signal'] = lt.fit_transform(test_chunks[4].copy(), 3 / 10, -162)
    test_chunks[6]['signal'] = lt.fit_transform(test_chunks[6].copy(), 3 / 10, -168)
    test_chunks[7]['signal'] = lt.fit_transform(test_chunks[7].copy(), 3 / 10, -171)
    test_chunks[8]['signal'] = lt.fit_transform(test_chunks[8].copy(), 3 / 10, -174)
    test_chunks[10]['signal'] = tt.fit_transform(test_chunks[10].copy(), 600, 50, 4.925)

    test_chunks = test_chunks[:10] + chunk_data(pd.concat(test_chunks[10:]), 10)
    return test_chunks