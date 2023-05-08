import math
import matplotlib.pyplot as plt
import pandas


def solve_incomplete_data(data):
    length = len(data)
    sum = 0.0
    for el in data:
        if not math.isnan(el):
            sum += el
    avg = sum / length
    for i in range(length):
        if math.isnan(data[i]) or data[i] == 0:
            data[i] = avg


def get_data(fileName):
    data = pandas.read_csv(fileName)
    input1 = [i for i in data['Economy.GDP.per.Capita']]
    solve_incomplete_data(input1)
    input2 = [i for i in data['Freedom']]
    solve_incomplete_data(input2)
    inputs = [input1, input2]
    outputs = [i for i in data['Happiness.Score']]
    return inputs, outputs


def plot_data_histograms(data, variable_name):
    plt.hist(data, 10)
    plt.title('Histogram of ' + variable_name)
    plt.show()

