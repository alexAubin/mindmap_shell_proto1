import networkx as nx

class NetworkLayout(object):
    """ List of positions for every node in a graph
    every element keeps a reference to a node of the baseGraph
    + functions to compute position list from a layout model
    """
    def __init__(self, baseGraph, firstLayoutType="stack" ):
        self.baseGraph = baseGraph
        self.nodesPositions = [ (node, [0, 0]) for node in self.baseGraph.nodes_iter(data=False) ]

    def basicLine(self):
        posx = 0
        for node in self.nodesPositions:
            node[1][0] = posx
            posx += 200

    def explicitPositionning(self, positionsList):
        i = 0
        for node in self.nodesPositions:
            if i < positionsList.__len__():
                node[1][0] = positionsList[i][0]
                node[1][1] = positionsList[i][1]
            i += 1

class NetworkMap(object):
    """Stores a graph with it's layouts in order to make it displayable"""
    def __init__(self, graph=None, defaultLayoutType="stack2", data=None, **attr):
        if graph == None:
            self.graph = nx.Graph(data, **attr)
        else:
            self.graph = graph
        self.layouts = [ NetworkLayout(self.graph, defaultLayoutType) ]


