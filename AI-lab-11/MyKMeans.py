import numpy as np

class MyKMeans:
    def __init__(self, no_clusters):
        self.__clusters = []
        self.__centroids = []
        self.__no_clusters = no_clusters

    def fit(self, train_inputs, no_epochs=1000):
        self.__centroids = self.__initiate_centroids(train_inputs)
        for _ in range(no_epochs):
            self.__clusters = [[] for _ in range(self.__no_clusters)]
            for input in train_inputs:
                computed_class = self.__get_min_distance(input)
                self.__clusters[computed_class].append(input)
            self.__centroids = [np.average(np.array(cluster), 0) for cluster in self.__clusters]
        return self

    def __get_min_distance(self, input):
        distances = [np.linalg.norm(np.array(input) - np.array(centroid)) for centroid in self.__centroids]
        computed_class = distances.index(min(distances))
        return computed_class

    def __initiate_centroids(self, train_inputs):
        indexes_for_centroids = np.random.choice(len(train_inputs), self.__no_clusters, replace=False)
        return [train_inputs[i] for i in indexes_for_centroids]

    def predict(self, inputs):
        return [self.__get_min_distance(input) for input in inputs]
