from networkMap import networkMap as nm
import networkx as nx

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class DrawGraphWidget(FloatLayout):

    def __init__(self, networkmap, **kwargs):
        super(DrawGraphWidget, self).__init__(**kwargs)
        for node in networkmap.layouts[0].nodesPositions:
            self.add_widget(Button(
                text=node[0],
                size_hint=(.1, .1),
                pos=(node[1][0], node[1][1] )))
            print(node[1][0])

class DrawGraphApp(App):
    def build(self):
        G = nx.Graph()
        G.add_nodes_from(["4"])
        G.add_nodes_from(["13"])
        G.add_nodes_from(["3564"])
        NM = nm.NetworkMap(G)
        return DrawGraphWidget(NM, size=(300, 300))


if __name__ == "__main__":
    DrawGraphApp().run()
