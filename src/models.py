import time
import pandas as pd
import numpy as np
import math
import random

from sklearn.model_selection import train_test_split, KFold, GroupKFold
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, StackingClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.metrics import f1_score

from keras.models import Sequential
from keras.layers import Dense, Conv1D, MaxPooling1D, Dropout, LSTM
from keras.regularizers import l1, l2, l1_l2

from src.sliding_window import *


sliding_window_size = None
            



class BasicNN():
    def __init__(self, window_size):
        self.window_size = window_size
        self.model = self._get_model()

    
    def _get_model(self):
        model = Sequential()
        model.add(Dense(22, input_dim = self.window_size, activation = 'relu'))
        model.add(Dense(33, activation = 'relu'))
        model.add(Dense(44, activation = 'relu'))
        model.add(Dense(11, activation = 'softmax'))
        model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model


    def fit(self, X, y, cycles = 5, epochs = 3):
        sliding_window_X = make_sliding_window_series(X, self.window_size)
        for _ in range(cycles):
            print('Cycle ' + str(_ + 1) + '/' + str(cycles))
            X_train, X_test, y_train, y_test = train_test_split(sliding_window_X, y, test_size = 0.35)
            self.model.fit(X_train, y_train, batch_size = 100, epochs = epochs, validation_data = (X_test, y_test))
        return self

    
    def predict(self, X):
        y_predictions = self.model.predict_classes(make_sliding_window_series(X, self.window_size))
        return y_predictions

        


class RNN():
    def __init__(self, window_size):
        self.window_size = window_size
        self.model = self._get_model()

    
    def _get_model(self):
        return model


    def fit(self, X, y, cycles = 5, epochs = 3):
        sliding_window_X = make_sliding_window_series(X, self.window_size)
        for _ in range(cycles):
            print('Cycle ' + str(_ + 1) + '/' + str(cycles))
            X_train, X_test, y_train, y_test = train_test_split(sliding_window_X, y, test_size = 0.35)
            self.model.fit(X_train, y_train, batch_size = 100, epochs = epochs, validation_data = (X_test, y_test))
        return self

    
    def predict(self, X):
        y_predictions = self.model.predict_classes(make_sliding_window_series(X, self.window_size))
        return y_predictions
        


        
        
        
        



class StackedNN():
    def __init__(self, window_size):
        self.window_size = window_size
        self.model = self._get_model()
    
    def _get_model(self):
        model = Sequential()
        model.add(Dense(22, input_dim = self.window_size, activation = 'relu'))
        model.add(Dense(33, activation = 'relu'))
        model.add(Dense(44, activation = 'relu'))
        model.add(Dense(11, activation = 'softmax'))
        model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model


    def fit(self, data, cycles = 5, epochs = 3):
        for _ in range(cycles):
            time.sleep(5)
            print('Cycle ' + str(_ + 1) + '/' + str(cycles))
            y = data['open_channels']
            X = data.drop(['open_channels'], axis = 1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.35)
            self.model.fit(X_train, y_train, batch_size = 100, epochs = epochs, validation_data = (X_test, y_test))
        return self


'''
def get_model(data, time_window_size):
    model = Sequential()
    model.add(Conv1D(filters=128, kernel_size=5, padding='same', activation='relu',
                         input_shape=(time_window_size, 1)))
    model.add(MaxPooling1D(pool_size=5))
    model.add(Dense(units = time_window_size, activation='linear'))
    model.add(Dense(time_window_size * 2, activation = 'relu'))
    model.add(Dense(11, activation = 'softmax'))
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
#'''

'''
def get_modelx(data, time_window_size):
    model = Sequential()
    model.add(LSTM(time_window_size * 10, input_shape  = (1, time_window_size)))
    model.add(Dense(40, activation = 'relu', kernel_regularizer = l2(0.01)))
    model.add(Dense(11, activation = 'softmax'))
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
#''';