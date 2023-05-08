import os

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import cdlib

from domain.GA import GA

"""
    Read a graph from a GML file.
    input: folder which contains the gml file with the same name
    output: networkx Graph object
"""


def readGraphFromGML(folderName):
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data', folderName, folderName + '.gml')
    return nx.read_gml(filePath, label='id')


"""
    Plot a network.
    input:
        network - networkx Graph object
        communities - list of every node's community
"""


def plotNetwork(network, communities=None):
    if communities is None:
        communities = [1 for i in range(network.number_of_nodes())]
    np.random.seed(123)  # to freeze the graph's view (networks uses a random view)
    pos = nx.spring_layout(network)  # compute graph layout
    plt.figure(figsize=(16, 16))
    nx.draw_networkx_nodes(network, pos, node_size=300, cmap=plt.cm.RdYlBu, node_color=communities)
    nx.draw_networkx_edges(network, pos, alpha=0.5)
    plt.show(network)


"""
    Maps the list of communities to a dictionary of communities as keys and nodes as values.
    input: list of communities
    output: dictionary of communities and nodes
"""


def mapNodesToCommunities(communities):
    communitiesNodes = dict()
    for i in range(len(communities)):
        if communities[i] in communitiesNodes:
            communitiesNodes[communities[i]].append(i + 1)
        else:
            communitiesNodes[communities[i]] = [i + 1]
    return communitiesNodes


"""
    Save the generated communities to file
"""


def saveCommunitiesToFile(folderName, communities):
    crtDir = os.getcwd()
    currentPath = os.path.join(crtDir, 'output')
    if not os.path.isdir(currentPath):
        os.mkdir(currentPath)
    currentPath = os.path.join(currentPath, folderName)
    if not os.path.isdir(currentPath):
        os.mkdir(currentPath)
    txtPath = os.path.join(currentPath, 'classLabel' + folderName + '.txt')
    with open(txtPath, 'w') as txtFile:
        for i in range(len(communities)):
            txtFile.write('{} {}\n'.format(i, communities[i]))
    datPath = os.path.join(currentPath, 'real.dat')
    with open(datPath, 'w') as datFile:
        communitiesNodes = mapNodesToCommunities(communities)
        for community in communitiesNodes.values():
            for node in community:
                datFile.write('{} '.format(node))
            datFile.write('\n')


"""
    Convert a list of communities to a list of sets of communities. 
    input: list of integers where every position represents the id of the node and every element represents the community id. 
    output: list of sets of integers, where every set represents a community and contains node ids. 
"""


def communitiesListToListOfSets(communities):
    commDict = dict()
    for i in range(len(communities)):
        if communities[i] in commDict.keys():
            commDict[communities[i]].add(i)
        else:
            commDict[communities[i]] = {i}
    listOfSets = []
    for commSet in commDict.values():
        listOfSets.append(commSet)
    return listOfSets


"""
    Find the communities inside a network by using a genetic algorithm with modularity as fitness function. 
    input: the networks - networkx graph, expectedModularity of the graph - double in range [-0.5, 1], expectedGenerations - integer 
    output: tuple consisting in the representation of the communities - list of integers and the modularity of this representation - double 
"""


def geneticAlgorithmCommunitiesDetectionModularity(network, expectedModularity, expectedGenerations):
    gaParam = {'popSize': 10, 'noGen': 1000}
    n = network.number_of_nodes()
    problParam = {'min': 0, 'max': n, 'noNodes': n, 'edges': network.edges,
                  'function': lambda x: nx.algorithms.community.modularity(network, communitiesListToListOfSets(x))}

    ga = GA(gaParam, problParam)
    ga.oneGenerationElitism()
    currentGen = 1
    while ga.bestChromosome().fitness <= expectedModularity and currentGen <= expectedGenerations:
        ga.oneGenerationElitism()
        currentGen += 1

    return ga.bestChromosome().repres, ga.bestChromosome().fitness


"""
    Plot and save to file all k communities from a network found in given directory using modularity-based genetic algorithm.
"""


def communitiesModularityGA(folderName, expectedModularity, expectedGenerations):
    network = readGraphFromGML(folderName)
    initialNetwork = readGraphFromGML(folderName)
    (communities, modularity) = geneticAlgorithmCommunitiesDetectionModularity(network, expectedModularity, expectedGenerations)
    plotNetwork(initialNetwork, communities)
    print('Modularity = {}'.format(modularity))
    saveCommunitiesToFile(folderName, communities)

    