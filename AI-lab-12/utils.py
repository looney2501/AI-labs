def load_emoticons():
    from skimage.io import imread_collection
    happy_collection = imread_collection('data/emoticons_images/happy_emoticons/*.png')
    sad_collection = imread_collection('data/emoticons_images/sad_emoticons/*.png')
    input_images = [happy_collection[i] for i in range(len(happy_collection))] + [sad_collection[i] for i in
                                                                                  range(len(sad_collection))]
    output_labels = ['happy' for _ in range(len(happy_collection))] + ['sad' for _ in range(len(sad_collection))]
    return input_images, output_labels


def load_face_images():
    import os
    angry_images = []
    for current_directory, dirnames, filenames in os.walk('data/face_images/angry'):
        for file in filenames:
            angry_images.append(os.path.join(current_directory, file))
    angry_images_outputs = ['angry' for _ in range(len(angry_images))]

    disgust_images = []
    for current_directory, dirnames, filenames in os.walk('data/face_images/disgust'):
        for file in filenames:
            disgust_images.append(os.path.join(current_directory, file))
    disgust_images_outputs = ['disgust' for _ in range(len(disgust_images))]

    fear_images = []
    for current_directory, dirnames, filenames in os.walk('data/face_images/fear'):
        for file in filenames:
            fear_images.append(os.path.join(current_directory, file))
    fear_images_outputs = ['fear' for _ in range(len(fear_images))]

    happy_images = []
    for current_directory, dirnames, filenames in os.walk('data/face_images/happy'):
        for file in filenames:
            happy_images.append(os.path.join(current_directory, file))
    happy_images_outputs = ['happy' for _ in range(len(happy_images))]

    neutral_images = []
    for current_directory, dirnames, filenames in os.walk('data/face_images/neutral'):
        for file in filenames:
            neutral_images.append(os.path.join(current_directory, file))
    neutral_images_outputs = ['neutral' for _ in range(len(neutral_images))]

    sad_images = []
    for current_directory, dirnames, filenames in os.walk('data/face_images/sad'):
        for file in filenames:
            sad_images.append(os.path.join(current_directory, file))
    sad_images_outputs = ['sad' for _ in range(len(sad_images))]

    surprise_images = []
    for current_directory, dirnames, filenames in os.walk('data/face_images/surprise'):
        for file in filenames:
            surprise_images.append(os.path.join(current_directory, file))
    surprise_images_outputs = ['surprise' for _ in range(len(surprise_images))]

    inputs = angry_images + disgust_images + fear_images + happy_images + neutral_images + sad_images + surprise_images
    outputs = angry_images_outputs + disgust_images_outputs + fear_images_outputs + happy_images_outputs + neutral_images_outputs + sad_images_outputs + surprise_images_outputs
    return inputs, outputs


def load_face_images_arrays():
    from skimage.io import imread_collection
    angry_images = [image for image in imread_collection('data/face_images/angry/*.jpg')]
    angry_images_outputs = ['angry' for _ in range(len(angry_images))]
    disgust_images = [image for image in imread_collection('data/face_images/disgust/*.jpg')]
    disgust_images_outputs = ['disgust' for _ in range(len(disgust_images))]
    fear_images = [image for image in imread_collection('data/face_images/fear/*.jpg')]
    fear_images_outputs = ['fear' for _ in range(len(fear_images))]
    happy_images = [image for image in imread_collection('data/face_images/happy/*.jpg')]
    happy_images_outputs = ['happy' for _ in range(len(happy_images))]
    neutral_images = [image for image in imread_collection('data/face_images/neutral/*.jpg')]
    neutral_images_outputs = ['neutral' for _ in range(len(neutral_images))]
    sad_images = [image for image in imread_collection('data/face_images/sad/*.jpg')]
    sad_images_outputs = ['sad' for _ in range(len(sad_images))]
    surprise_images = [image for image in imread_collection('data/face_images/surprise/*.jpg')]
    surprise_images_outputs = ['surprise' for _ in range(len(surprise_images))]
    inputs = angry_images + disgust_images + fear_images + happy_images + neutral_images + sad_images + surprise_images
    outputs = angry_images_outputs + disgust_images_outputs + fear_images_outputs + happy_images_outputs + neutral_images_outputs + sad_images_outputs + surprise_images_outputs
    return inputs, outputs


def load_face_images_arrays_rgb():
    from skimage.color import gray2rgb
    inputs, outputs = load_face_images_arrays()
    inputs = [gray2rgb(image) for image in inputs]
    return inputs, outputs


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


def extract_features(image):
    from skimage.feature import haar_like_feature
    return haar_like_feature(image, 11, 11, image.shape[0] // 4, image.shape[1] // 4)
