
# MOMINA ATIF DAR   P18-0030


import networkx as nx
import matplotlib.pyplot as plt

#%matplotlib inline 
import warnings
warnings.filterwarnings("ignore")

def draw_graph_with_nx(G): 
    pos = nx.spring_layout(G, iterations=200)
    options = {'node_color': 'white', 'alpha': 1, 'node_size': 2000, 'width': 0.002, 'font_color': 'darkred', 
               'font_size': 25, 'arrows': True, 'edge_color': 'brown',
               'arrowstyle': 'Fancy, head_length=1, head_width=1, tail_width=.4'
              }
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, labels=labels,  **options)
    plt.show()
    
    
class Digraph:
    def __init__(self):
        self.g = {}
        
    def add_node(self,node):
        if node in self.g:
            raise ValueError("Source already exists")

        self.g[node] = []
        
    def add_edge(self,src,dest):
        if src not in self.g and dest not in self.g:
            raise ValueError('Source/Destination not found')

        edges = self.g[src]

        if dest not in edges:
            edges.append(dest)
        
        else:
            raise ValueError("Destination already exists")

    def draw_graph(self): 
        G = nx.DiGraph()
        for src in self.g: 
            G.add_node(src, label=src) 
            for dest in self.g[src]:
                G.add_edge(src, dest)
                
        draw_graph_with_nx(G)
        
        
if __name__ == '__main__':
    g = Digraph()
    g.add_node('Isd')
    g.add_node('Pwr')
    g.add_node('Grw')
    g.add_node('Lhr')
    g.add_node('Fsd')
    
    g.add_edge('Isd','Pwr')
    g.add_edge('Isd','Lhr')
    
    g.draw_graph()
