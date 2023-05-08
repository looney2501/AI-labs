from math import exp
from numpy.linalg import inv
import numpy as np


class MyLogisticRegression:
    def __init__(self):
        self.intercept_ = []
        self.coef_ = []

    def fit(self, x, y, learning_rate=0.001, no_epochs=1000):
        no_classes = len(set(y))
        if no_classes == 2:
            coef = [0.0 for _ in range(1 + len(x[0]))]
            for epoch in range(no_epochs):
                for i in range(len(x)):
                    ycomputed = self.sigmoid(self.eval(x[i], coef))
                    current_error = ycomputed - y[i]
                    for j in range(0, len(x[0])):
                        coef[j + 1] = coef[j + 1] - learning_rate * current_error * x[i][j]
                    coef[0] = coef[0] - learning_rate * current_error * 1
            self.intercept_.append(coef[0])
            self.coef_.append(coef[1:])
        else:
            y_for_class = [[el for el in y] for _ in range(no_classes)]
            for i in range(no_classes):
                for j in range(len(y_for_class[0])):
                    if y_for_class[i][j] == i:
                        y_for_class[i][j] = 1
                    else:
                        y_for_class[i][j] = 0
            all_coef = [[0.0 for _ in range(1 + len(x[0]))] for _ in range(no_classes)]
            for i in range(no_classes):
                for epoch in range(no_epochs):
                    for j in range(len(x)):
                        ycomputed = self.sigmoid(self.eval(x[j], all_coef[i]))
                        current_eror = ycomputed - y_for_class[i][j]
                        for k in range(len(x[0])):
                            all_coef[i][k + 1] -= learning_rate * current_eror * x[j][k]
                        all_coef[i][0] -= learning_rate * current_eror
                self.intercept_.append(all_coef[i][0])
                self.coef_.append(all_coef[i][1:])

    @staticmethod
    def eval(xi, coef):
        yi = coef[0]
        for j in range(len(xi)):
            yi += coef[j + 1] * xi[j]
        return yi

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + exp(-x))

    def __predictOneSample(self, sample_features):
        threshold = 0.5
        no_regressors = len(self.intercept_)
        coefficients = [[self.intercept_[i]] + [c for c in self.coef_[i]] for i in range(no_regressors)]
        if no_regressors == 1:
            computed_float_value = self.eval(sample_features, coefficients[0])
            computed_unit_value = self.sigmoid(computed_float_value)
            computed_label = 0 if computed_unit_value < threshold else 1
            return computed_label
        else:
            computed_float_values = [self.eval(sample_features, coefficients[i]) for i in range(no_regressors)]
            computed_unit_values = [self.sigmoid(el) for el in computed_float_values]
            return computed_unit_values.index(max(computed_unit_values))


    def predict(self, inputs):
        computed_labels = [self.__predictOneSample(sample) for sample in inputs]
        return computed_labels