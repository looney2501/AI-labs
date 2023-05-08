import numpy
import pandas
import matplotlib.pyplot as plt
import sklearn.datasets


def get_data(file_name, column_name):
    data = pandas.read_csv(file_name)
    data = [i for i in data[column_name]]
    return data


def split_data_into_training_and_validation(inputs, outputs, split_coeff):
    no_inputs = len(inputs[0])
    indexes = [i for i in range(no_inputs)]

    train_indexes = numpy.random.choice(indexes, int(split_coeff * no_inputs), replace=False)
    validation_indexes = [i for i in indexes if not i in train_indexes]

    train_inputs = []
    for i in range(len(inputs)):
        current_train_inputs = [inputs[i][j] for j in train_indexes]
        train_inputs.append(current_train_inputs)

    train_outputs = [outputs[i] for i in train_indexes]

    validation_inputs = []
    for i in range(len(inputs)):
        current_validation_inputs = [inputs[i][j] for j in validation_indexes]
        validation_inputs.append(current_validation_inputs)
    validation_outputs = [outputs[i] for i in validation_indexes]

    return train_inputs, train_outputs, validation_inputs, validation_outputs


def plot_data_histograms(data, variable_name):
    plt.hist(data, 10)
    plt.title('Histogram of ' + variable_name)
    plt.show()


def statistical_normalisation(features):
    mean_value = sum(features) / len(features)
    std_dev = (1 / len(features) * sum([(feat - mean_value) ** 2 for feat in features])) ** 0.5
    normalised_features = [(feat - mean_value) / std_dev for feat in features]
    return normalised_features


def get_linnerud_data():
    linnerud_dataset = sklearn.datasets.load_linnerud(as_frame=True)

    features_names = linnerud_dataset.feature_names
    inputs = []
    features = linnerud_dataset.data
    for i in range(len(features_names)):
        data = [el for el in features[features_names[i]]]
        inputs.append(data)

    targets_names = linnerud_dataset.target_names
    outputs = []
    targets = linnerud_dataset.target
    for i in range(len(targets_names)):
        data = [el for el in targets[targets_names[i]]]
        print(data)
        outputs.append(data)

    return inputs, outputs


def split_data_into_training_and_validation_multi_target(inputs, outputs, split_coeff):
    no_inputs = len(inputs[0])
    indexes = [i for i in range(no_inputs)]

    train_indexes = numpy.random.choice(indexes, int(split_coeff * no_inputs), replace=False)
    validation_indexes = [i for i in indexes if not i in train_indexes]

    train_inputs = []
    for i in range(len(inputs)):
        current_train_inputs = [inputs[i][j] for j in train_indexes]
        train_inputs.append(current_train_inputs)

    train_outputs = []
    for i in range(len(outputs)):
        current_train_outputs = [outputs[i][j] for j in train_indexes]
        train_outputs.append(current_train_outputs)

    validation_inputs = []
    for i in range(len(inputs)):
        current_validation_inputs = [inputs[i][j] for j in validation_indexes]
        validation_inputs.append(current_validation_inputs)

    validation_outputs = []
    for i in range(len(outputs)):
        current_validation_outputs = [outputs[i][j] for j in validation_indexes]
        validation_outputs.append(current_validation_outputs)

    return train_inputs, train_outputs, validation_inputs, validation_outputs
