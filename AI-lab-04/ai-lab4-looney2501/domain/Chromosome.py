from numpy.random import randint


class Chromosome:

    def __init__(self, problParam=None):
        self.__fitness = 0.0
        self.__problParam = problParam
        self.__repres = self.initialiseRepres()
        self.__weightedAdjList = problParam["weightedAdjList"]

    def initialiseRepres(self):
        repres = [i for i in range(self.__problParam["noNodes"])]
        p1 = randint(self.__problParam["noNodes"])
        p2 = randint(self.__problParam["noNodes"])
        repres[p1], repres[p2] = repres[p2], repres[p1]
        return repres

    @property
    def repres(self):
        return self.__repres

    @repres.setter
    def repres(self, l=None):
        if l is None:
            l = []
        self.__repres = l

    @property
    def fitness(self):
        return self.__fitness

    @fitness.setter
    def fitness(self, value):
        self.__fitness = value

    @property
    def weightedAdjList(self):
        return self.__weightedAdjList

    def crossover(self, c):
        n = self.__problParam["noNodes"]
        p1 = self.__repres
        p2 = c.__repres
        offspringRepres = []
        for i in range(n):
            offspringRepres.append(p2[p1[i]])
        offspring = Chromosome(self.__problParam)
        offspring.repres = offspringRepres
        return offspring

    def mutation(self):
        p1 = randint(self.__problParam["noNodes"])
        p2 = randint(self.__problParam["noNodes"])
        self.__repres[p1], self.__repres[p2] = self.__repres[p2], self.__repres[p1]

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
