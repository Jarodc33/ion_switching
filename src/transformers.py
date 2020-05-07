import numpy as np
import pandas as pd
import math

class LinearTransformation():
    """
    This class is able to subtract off a linear function from data assuming the first column is x and the second is y
    """
    def __init__(self):
        pass
    
    
    def fit(self, slope, intercept):
        self.slope = slope
        self.intercept = intercept
        return self
    
    
    def transform(self, data):
        array = np.array(data)
        x = array[:, 0]
        y = array[:, 1]
        return y - (self.slope * x + self.intercept)
    
    
    def fit_transform(self, data, slope, intercept):
        self.fit(slope, intercept)
        return self.transform(data)

    
    
class ParabolicTransformation():
    """
    This class is able to subtract off a parabolic function from data assuming the first column is x and the second is y
    """
    def __init__(self):
        pass
    
    
    def fit(self, a, h, k):
        self.a = a
        self.h = h
        self.k = k
        return self
    
    
    def transform(self, data):
        array = np.array(data)
        x = array[:, 0]
        y = array[:, 1] 
        return y - (self.a * (x - self.h) ** 2 + self.k)
    
    
    def fit_transform(self, data, a, h, k):
        self.fit(a, h, k)
        return self.transform(data)
    
    
    
class TrigTransformation():
    """
    This class is able to subtract off a trig function from data assuming the first column is x and the second is y
    """
    def __init__(self, trig_function : str):
        self.function = exec('math.' + trig_function)
    
    
    def fit(self, start, period, height):
        self.start = start
        self.period = period
        self.height = height
        return self
    
    
    def transform(self, data):
        array = np.array(data)
        x = array[:, 0]
        y = array[:, 1] 
        x = pd.Series(x)
        return y - x.apply(lambda x: self.height * math.sin((x - self.start) * math.pi / self.period)).values
    
    
    def fit_transform(self, data, start, period, height):
        self.fit(start, period, height)
        return self.transform(data)
    
    
    
class MeanTransformer():
    """
    This class will transform a dataset to have the mean of another data set. If the training data is a number then the mean will be transformed to that number
    """
    def __init__(self):
        pass
    
    
    def fit(self, training_data):
        self.mean = np.array(training_data).mean()
        return self
    
    
    def transform(self, data):
        mean = np.array(data).mean()
        return data.copy() - (mean - self.mean)
    
    
    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)