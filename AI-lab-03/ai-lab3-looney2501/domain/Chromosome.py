from numpy.random import randint, choice


class Chromosome:

    def __init__(self, problParam=None):
        self.__fitness = 0.0
        self.__problParam = problParam
        self.__initRepresentation()

    def __initRepresentation(self):
        self.__repres = [randint(self.__problParam['min'], self.__problParam['max'] + 1) for _ in
                         range(self.__problParam['noNodes'])]
        twentyPercent = int(0.2 * self.__problParam['noNodes'])
        if twentyPercent == 0:
            twentyPercent = 1
        twentyPercentOfNodes = [list(choice(self.__problParam['noNodes'] - 1, twentyPercent, replace=False))]
        edges = self.__problParam['edges']
        for el in twentyPercentOfNodes:
            for edge in edges:
                if edge[0] == el or edge[1] == el:
                    self.__repres[edge[0]] = self.__repres[el]
                    self.__repres[edge[1]] = self.__repres[el]

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @fitness.setter
    def fitness(self, value):
        self.__fitness = value

    @repres.setter
    def repres(self, l=None):
        if l is None:
            l = []
        self.__repres = l

    def crossover(self, c):
        source = self.__repres
        destination = c.__repres
        newrepres = []
        randNode = randint(0, self.__problParam['noNodes'])
        randNodeCommunity = source[randNode]
        for i in range(self.__problParam['noNodes']):
            if source[i] == randNodeCommunity:
                newrepres.append(randNodeCommunity)
            else:
                newrepres.append(destination[i])
        offspring = Chromosome(c.__problParam)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        pos = randint(0, self.__problParam['noNodes'])
        self.__repres[pos] = randint(1, max(self.__repres) + 1)

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
