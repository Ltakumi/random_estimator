from sklearn.base import BaseEstimator
import numpy as np
import pandas as pd

class MyRandomRegressor(BaseEstimator):
    """This model predicts random values between the mininimum and the maximum of y"""

    def fit(self, X, y):
        self.y_range = [np.min(y), np.max(y)]

    def predict(self, X):
        return np.random.uniform(self.y_range[0], self.y_range[1], size=X.shape[0])

