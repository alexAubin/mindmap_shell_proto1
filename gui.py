from networkMap import networkMap as nm
import networkx as nx

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Bezier, Line

class DrawGraphWidget(FloatLayout):

    def __init__(self, networkmap, **kwargs):
        super(DrawGraphWidget, self).__init__(**kwargs)

        self.DrawAllLinks(networkmap)

        for node in networkmap.layouts[0].nodesPositions:
            self.add_widget(Button(
                text=node[0],
                size_hint=(.1, .1),
                pos=(node[1][0], node[1][1] )))
            print(node[1][0])


    def DrawAllLinks(self, networkMap) :
        G = networkMap.graph
        for edge in G.edges_iter() :
            self.DrawLink(networkMap.layouts[0].nodesPositions, edge[0], edge[1])

    def GetNodeInLayout(self, layout, nodeName) :
        for node in layout :
            if (node[0] == nodeName) :
                return node

        print "Could find node " + nodeName + " in the following layout : "
        print layout

    def DrawLink(self, layout, nodeBeginName, nodeEndName) :

        nodeBegin = self.GetNodeInLayout(layout,nodeBeginName)
        nodeEnd   = self.GetNodeInLayout(layout,nodeEndName)

        buttonSize = 50

        xBegin = nodeBegin[1][0] + buttonSize/2
        xEnd   = nodeEnd[1][0]   + buttonSize/2

        yBegin = nodeBegin[1][1] + buttonSize/2
        yEnd   = nodeEnd[1][1]   + buttonSize/2

        xMid = (xBegin + xEnd) / 2
        yMid = (yBegin + yEnd) / 2

        points = [ xBegin, yBegin ]

        if (xMid > yMid) :
            points.extend( [ xMid,  yBegin ] )
            points.extend( [ xMid,  yMid  ] )
            points.extend( [ xMid,  yEnd  ] )
        else :
            points.extend( [ xBegin, yMid ] )
            points.extend( [ xMid,   yMid  ] )
            points.extend( [ xEnd,   yMid  ] )
        points.extend( [ xEnd,  yEnd ] )

        with self.canvas:
            Color(1.0, 0.0, 0.0)
            self.bezier = Bezier(points=points, segments=150)

class DrawGraphApp(App):
    def build(self):
        G = nx.Graph()
        G.add_nodes_from(["4"])
        G.add_nodes_from(["13"])
        G.add_nodes_from(["3564"])
        G.add_edge("13","4")
        G.add_edge("4","3564")
        NM = nm.NetworkMap(G)
        NM.layouts[0].explicitPositionning([[50, 50], [150, 150], [250, 250], [350, 350]])
        return DrawGraphWidget(NM, size=(300, 300))


if __name__ == "__main__":
    DrawGraphApp().run()
