import networkx
from aco_utils.ant import Ant

"""
    Abstract data type used for executing Ant System algorithms.
"""


class AntColony:
    """
    Constructor for an AntColony object, requiring a neworkx Graph object, a value for the colony size
    and two values for the interval of pheromone values.
    """

    def __init__(self, network: networkx.Graph, colony_size, ph_min, ph_max, pheromone_evaporation_coeff, alpha, beta):
        self.__network = network
        self.__colony_size = colony_size
        self.__colony = None
        self.__ph_min = ph_min
        self.__ph_max = ph_max
        self.__pheromone_values = None
        self.__pheromone_evaporation_coeff = pheromone_evaporation_coeff
        self.__alpha = alpha
        self.__beta = beta

    """
        Initializes the ant colony.
    """
    def initialize(self):
        n = self.__network.number_of_nodes()
        self.__pheromone_values = [[(self.__ph_max + self.__ph_min) / 2] * n] * n
        self.__colony = [Ant(self.__network, self.__pheromone_values) for _ in range(self.__colony_size)]

    """
        Generates the paths by iterating once the AS algorithm.
    """
    def __generate_paths(self):
        for ant in self.__colony:
            ant.initialize_path()
        for _ in range(self.__network.number_of_nodes() - 1):
            for ant in self.__colony:
                ant.move(self.__alpha, self.__beta)

    """
        Updates the pheromone values. Has to be done after a complete path generation.
    """
    def __update_pheromone_values(self):
        best_ant = self.best_ant()
        best_weight = self.fitness(best_ant)
        added_pheromone = 1 / best_weight
        n = self.__network.number_of_nodes()
        for i in range(n):
            for j in range(n):
                new_pheromone = self.__pheromone_values[i][j] * (1 - self.__pheromone_evaporation_coeff)
                for k in range(0, n):
                    if best_ant.path[k-1] == i+1 and best_ant.path[k] == j+1 or best_ant.path[k-1] == j+1 and best_ant.path[k] == i+1:
                        new_pheromone += added_pheromone
                        break
                if new_pheromone > self.__ph_max:
                    new_pheromone = self.__ph_max
                if new_pheromone < self.__ph_min:
                    new_pheromone = self.__ph_min
                self.__pheromone_values[i][j] = new_pheromone
                self.__pheromone_values[j][i] = new_pheromone

    """
        Gets the ant from the colony which has the lowest value for its fitness.
        @:return: Ant object 
    """
    def best_ant(self):
        return min(self.__colony, key=self.fitness)

    """
        Gets the fitness of an ant. The fitness represents the weight of the path travelled by the ant.
        @:return: integer representing the fitness of the ant
    """
    def fitness(self, best_ant:Ant):
        weight = 0
        for i in range(self.__network.number_of_nodes() - 1):
            n1 = best_ant.path[i]
            n2 = best_ant.path[i + 1]
            weight += self.__network[n1][n2]['weight']
        weight += self.__network[best_ant.path[-1]][best_ant.path[0]]['weight']
        return weight

    """
        Executes the AS algorithm once. The colony must be initialized before.
    """
    def execute_once(self):
        self.__generate_paths()
        self.__update_pheromone_values()
