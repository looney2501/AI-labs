import networkx
from numpy.random import randint, choice

"""
    An Ant randomly chooses its path in a network, based on pheromone quantity of the edges and their weight.  
"""


class Ant:
    """
        Constructor of an Ant object, requiring a networkx Graph object and a matrix of pheromone values.
        @:param: network - networkx Graph with weighted edges
        @:param: pheromone_values: - matrix of pheromones
    """

    def __init__(self, network: networkx.Graph, pheromone_values):
        self.__network = network
        self.__pheromone_values = pheromone_values
        self.__path = None

    """
        Initializes the path of the Ant, placing it on a position.
    """

    def initialize_path(self):
        self.__path = []
        self.__path.append(randint(1, self.__network.number_of_nodes() + 1))

    """
        Moves the Ant to a new position.
    """

    def move(self, alpha, beta):
        probabilities = self.__generate_probabilities(alpha, beta)
        sumProb = sum(probabilities)
        if sumProb == 0:
            print(sumProb)
        next_node = choice(self.__network.nodes, p=probabilities)
        self.__path.append(next_node)

    """
        Gets the probabilities of choosing every node from the current position.
        @:return: list of probabilities  
    """

    def __generate_probabilities(self, alpha, beta):
        probabilities = []
        probabilities_sum = 0.0
        i = self.__path[-1]

        for j in self.__network.nodes:
            if j in self.__path:
                probability = 0
            else:
                pheromone = self.__pheromone_values[i-1][j-1]
                probability = pheromone ** alpha * (1 / self.__network[i][j]['weight']) ** beta
            probabilities_sum += probability

        for j in self.__network.nodes:
            if j in self.__path:
                probability = 0
            else:
                pheromone = self.__pheromone_values[i - 1][j - 1]
                probability = pheromone ** alpha * (1 / self.__network[i][j]['weight']) ** beta / probabilities_sum
            probabilities.append(probability)
        return probabilities

    @property
    def path(self):
        return self.__path
