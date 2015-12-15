import networkx as nx



class NetworkLayout(object):
    """ List of positions for every node in a graph
    every element keeps a reference to a node of the baseGraph
    + functions to compute position list from layout model
    """
    def __init__(self, baseGraph, firstLayoutType="stack" ):
        self.baseGraph = baseGraph
        self.nodesPositions = self.computePositions(firstLayoutType)

    def computePositions(self, layoutType = "stack"):
        positionsList = []
        if layoutType == "stack":
            positionsList = [ (node, (0, 0)) for node in self.baseGraph.nodes_iter(data=False) ]
            print(positionsList)
        if layoutType == "stack2":
            posx = 50
            positionsList = []
            for node in self.baseGraph.nodes_iter(data=False):
                positionsList.append((node,(posx,0)))
                posx += 50
            print(positionsList)
        return positionsList

    def explicitPositionning(self, positionsList):
        '''self.nodesPositions = [ (node, position) for  ]'''
        pass

class NetworkMap(object):
    """Stores a graph with it's layouts in order to make it displayable"""
    def __init__(self, graph=None, defaultLayoutType="stack2", data=None, **attr):
        if graph == None:
            self.graph = nx.Graph(data, **attr)
        else:
            self.graph = graph
        self.layouts = [ NetworkLayout(self.graph, defaultLayoutType) ]


