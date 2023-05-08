def sepia_pixel(pixel):
    R = pixel[0]
    G = pixel[1]
    B = pixel[2]
    tr = 0.393 * R + 0.769 * G + 0.189 * B
    tg = 0.349 * R + 0.686 * G + 0.168 * B
    tb = 0.272 * R + 0.534 * G + 0.131 * B
    pixel[0] = min(255, int(tr))
    pixel[1] = min(255, int(tg))
    pixel[2] = min(255, int(tb))


def sepia(image):
    dimensions = image.shape[0], image.shape[1]
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            sepia_pixel(image[i][j])
    return image


def load_sepia():
    from skimage.io import imread_collection
    img_collection = imread_collection('data/*.png')
    no_images = len(img_collection)
    indexes = [i for i in range(no_images)]
    from numpy.random import choice
    sepia_images_indexes = choice(indexes, int(0.5 * len(img_collection)), replace=False)
    img_collection = [sepia(img_collection[i]) if i in sepia_images_indexes else img_collection[i] for i in indexes]
    output_labels = [1 if i in sepia_images_indexes else 0 for i in indexes]
    return img_collection, output_labels


def plot_data_histograms(data, variable_name):
    import matplotlib.pyplot as plt
    plt.hist(data, 10)
    plt.title('Histogram of ' + variable_name)
    plt.show()


def split_data_into_training_and_validation(inputs, outputs, split_coeff):
    from numpy.random import choice
    no_inputs = len(inputs)
    indexes = [i for i in range(no_inputs)]

    train_indexes = choice(indexes, int(split_coeff * no_inputs), replace=False)
    validation_indexes = [i for i in indexes if not i in train_indexes]

    train_inputs = [inputs[i] for i in train_indexes]
    train_outputs = [outputs[i] for i in train_indexes]

    validation_inputs = [inputs[i] for i in validation_indexes]
    validation_outputs = [outputs[i] for i in validation_indexes]

    return train_inputs, train_outputs, validation_inputs, validation_outputs


def flatten_matrix(mat):
    from numpy import ndarray
    x = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if isinstance(mat[i][j], (list, ndarray)):
                x += [el for el in mat[i][j]]
            else:
                x.append(mat[i][j])
    return x


def normalisation(trainData, testData):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    if not isinstance(trainData[0], list):
        # encode each sample into a list
        trainData = [[d] for d in trainData]
        testData = [[d] for d in testData]

        scaler.fit(trainData)  # fit only on training data
        normalisedTrainData = scaler.transform(trainData)  # apply same transformation to train data
        normalisedTestData = scaler.transform(testData)  # apply same transformation to test data

        # decode from list to raw values
        normalisedTrainData = [el[0] for el in normalisedTrainData]
        normalisedTestData = [el[0] for el in normalisedTestData]
    else:
        scaler.fit(trainData)  # fit only on training data
        normalisedTrainData = scaler.transform(trainData)  # apply same transformation to train data
        normalisedTestData = scaler.transform(testData)  # apply same transformation to test data
    return normalisedTrainData, normalisedTestData


def plot_confusion_matrix(cm, classNames, title):
    import matplotlib.pyplot as plt
    import itertools
    import numpy as np

    classes = classNames
    plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap='Blues')
    plt.title('Confusion Matrix ' + title)
    plt.colorbar()
    tick_marks = np.arange(len(classNames))
    plt.xticks(tick_marks, classNames, rotation=45)
    plt.yticks(tick_marks, classNames)

    text_format = 'd'
    thresh = cm.max() / 2.
    for row, column in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(column, row, format(cm[row, column], text_format),
                 horizontalalignment='center',
                 color='white' if cm[row, column] > thresh else 'black')

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

    plt.show()
