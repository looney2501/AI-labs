class MyBGDRegressor:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    def fit(self, x, y, learning_rate=0.01, no_epochs=1000):
        self.coef_ = [0.0 for _ in range(len(x[0]) + 1)]
        no_samples = len(x)
        for epoch in range(no_epochs):
            mean_error = 0.0
            for i in range(no_samples):
                ycomputed = self.__eval(x[i])
                mean_error += ycomputed - y[i]
            mean_error /= no_samples
            for i in range(no_samples):
                for j in range(len(x[0])):
                    self.coef_[j] = self.coef_[j] - learning_rate * mean_error * x[i][j]
                self.coef_[len(x[0])] = self.coef_[len(x[0])] - learning_rate * mean_error

        self.intercept_ = self.coef_[-1]
        self.coef_ = self.coef_[:-1]

    def __eval(self, xi):
        yi = self.coef_[-1]
        for j in range(len(xi)):
            yi += self.coef_[j] * xi[j]
        return yi

    def predict(self, x):
        ycomputed = [self.__eval(xi) for xi in x]
        return ycomputed
