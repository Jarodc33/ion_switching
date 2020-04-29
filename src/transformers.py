import numpy as np
import pandas as pd
import math

class LinearTransformation():
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
    
    
    
