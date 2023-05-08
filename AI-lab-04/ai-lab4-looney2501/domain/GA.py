from numpy.random import randint
from domain.Chromosome import Chromosome


class GA:

    def __init__(self, param=None, problParam=None):
        self.__param = param
        self.__problParam = problParam
        self.__initialisePopulation()

    def __initialisePopulation(self):
        self.__population = []
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__problParam)
            self.__population.append(c)

    def __evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](c)

    @property
    def population(self):
        return self.__population

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best
    
    def worstChromosome(self):
        worst = self.__population[0]
        for c in self.__population:
            if c.fitness > worst.fitness:
                worst = c
        return worst

    def selection(self):
        pos1 = randint(0, self.__param['popSize'])
        pos2 = randint(0, self.__param['popSize'])
        if (self.__population[pos1].fitness > self.__population[pos2].fitness):
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.__evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['popSize'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.__evaluation()
        
    def oneGenerationSteadyState(self):
        p1 = self.__population[self.selection()]
        p2 = self.__population[self.selection()]
        off = p1.crossover(p2)
        off.mutation()
        off.fitness = self.__problParam['function'](off)
        worst = self.worstChromosome()
        if off.fitness < worst.fitness:
            self.__population.remove(worst)
            self.__population.append(off)
        self.__evaluation()
        
