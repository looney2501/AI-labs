import copy


class MyRegressor:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = [0.0, 0.0]

    @staticmethod
    def __multiply_matrix(a, b):
        no_lines = len(a)
        no_columns = len(b[0])
        result = []
        for i in range(no_lines):
            result.append([])
            for j in range(no_columns):
                result[i].append(0)

        for i in range(no_lines):
            for j in range(no_columns):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]

        return result

    @staticmethod
    def __transpose(x):
        x_transposed = [[], [], []]
        for i in range(len(x)):
            x_transposed[0].append(x[i][0])
            x_transposed[1].append(x[i][1])
            x_transposed[2].append(x[i][2])

        return x_transposed

    @staticmethod
    def __inverse(x):
        x_copy = copy.deepcopy(x)
        for i in range(3):
            for j in range(3):
                if i == j:
                    x_copy[i].append(1)
                else:
                    x_copy[i].append(0)

        if x_copy[1][0] != 0:
            coeff = x_copy[1][0] / x_copy[0][0]
            for i in range(6):
                x_copy[1][i] -= coeff * x_copy[0][i]

        if x_copy[2][0] != 0:
            coeff = x_copy[2][0] / x_copy[0][0]
            for i in range(6):
                x_copy[2][i] -= coeff * x_copy[0][i]

        if x_copy[2][1] != 0:
            coeff = x_copy[2][1] / x_copy[1][1]
            for i in range(6):
                x_copy[2][i] -= coeff * x_copy[1][i]

        if x_copy[1][2] != 0:
            coeff = x_copy[1][2] / x_copy[2][2]
            for i in range(6):
                x_copy[1][i] -= coeff * x_copy[2][i]

        if x_copy[0][2] != 0:
            coeff = x_copy[0][2] / x_copy[2][2]
            for i in range(6):
                x_copy[0][i] -= coeff * x_copy[1][i]

        if x_copy[0][1] != 0:
            coeff = x_copy[0][1] / x_copy[1][1]
            for i in range(6):
                x_copy[0][i] -= coeff * x_copy[1][i]

        for i in range(3):
            if x_copy[i][i] != 1:
                coeff = x_copy[i][i]
                for j in range(6):
                    x_copy[i][j] /= coeff

        result = [x_copy[i][3:6] for i in range(3)]
        return result

    def fit(self, x, y):
        x_augmented = [[1, el[0], el[1]] for el in x]
        x_augmented_transposed = self.__transpose(x_augmented)
        first_multiplication = self.__multiply_matrix(x_augmented_transposed, x_augmented)
        second_multiplication = self.__multiply_matrix(self.__inverse(first_multiplication), x_augmented_transposed)
        y_modified = [[el] for el in y]
        w = self.__multiply_matrix(second_multiplication, y_modified)
        self.intercept_ = w[0][0]
        self.coef_[0] = w[1][0]
        self.coef_[1] = w[2][0]

    def predict(self, x):
        return [self.intercept_ + self.coef_[0] * val[0] + self.coef_[1] * val[1] for val in x]