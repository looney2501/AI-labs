import numpy as np


def softmax(X):
    from math import exp
    exp_values = [exp(val) for val in X]
    return [val / sum(exp_values) for val in exp_values]


def sigmoid(gamma):
    import math
    if gamma < 0:
        return 1 - 1 / (1 + math.exp(gamma))
    else:
        return 1 / (1 + math.exp(-gamma))


def sigmoid_derivative(x):
    f = sigmoid(x)
    return f * (1 - f)


class NeuralNetwork:
    def __initialise(self, x, y, l):
        self.__learning_rate = l
        self.__inputs = x
        self.__no_features = len(self.__inputs[0])
        self.__no_outputs = max(y) + 1
        self.__real_outputs = y
        self.__layer1 = [0 for _ in range(5)]
        self.__outputs = [0 for _ in range(self.__no_outputs)]
        # linii - nr de outputuri; coloane - nr de inputuri
        self.__weights1 = [[np.random.random() for _ in range(self.__no_features)] for _ in range(len(self.__layer1))]
        self.__weights2 = [[np.random.random() for _ in range(len(self.__layer1))] for _ in range(self.__no_outputs)]

    def __loss_function_derivative(self, i):
        grad = softmax(self.__outputs)
        grad[self.__real_outputs[i]] -= 1
        return grad

    def __feedforward(self, i):
        for j in range(len(self.__layer1)):
            value = 0
            for k in range(self.__no_features):
                value += self.__inputs[i][k] * self.__weights1[j][k]
            self.__layer1[j] = sigmoid(value)
        for j in range(self.__no_outputs):
            value = 0
            for k in range(len(self.__layer1)):
                value += self.__layer1[k] * self.__weights2[j][k]
            self.__outputs[j] = value
        self.__outputs = softmax(self.__outputs)

    def __backprop(self, i):
        for j in range(self.__no_outputs):
            loss_function_value = self.__loss_function_derivative(i)
            for k in range(len(self.__layer1)):
                delta_weight = loss_function_value[j] * self.__layer1[k]
                self.__weights2[j][k] += self.__learning_rate * delta_weight

        for j in range(self.__no_outputs):
            loss_function_value = self.__loss_function_derivative(i)
            for k in range(len(self.__layer1)):
                sigmoid_derivative_layer1 = sigmoid_derivative(self.__layer1[k])
                for l in range(self.__no_features):
                    delta_weight = loss_function_value[j] * self.__weights2[j][k] * sigmoid_derivative_layer1 * \
                                   self.__inputs[i][l]
                    self.__weights1[k][l] += self.__learning_rate * delta_weight

    def fit(self, x, y, learning_rate=0.001, no_epochs=100):
        self.__initialise(x, y, learning_rate)
        for i in range(no_epochs):
            for j in range(len(self.__inputs)):
                self.__feedforward(j)
                self.__backprop(j)

    def predict(self, x):
        self.__inputs = x
        computed_labels = []
        for i in range(len(x)):
            self.__feedforward(i)
            computed_labels.append(np.argmax(self.__outputs))
        return computed_labels
