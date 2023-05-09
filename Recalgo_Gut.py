import networkx as nx
import matplotlib.pyplot as plt
import itertools
from mcs import mcs,cliqueCutsets
from But import is_But

gut =[('1', '3'), ('1', '4'),('1','6'), ('2', '3'),('2', '7'),('3','8'),('3','6'),('3', '4'), ('4', '5'),('4','9'),
      ('4','6'),('5','10'),('7','8'),('8','11'),('11','9'),('9','10')] # gut graph

connections=[('a', 'b'),
                   ('a', 'd'),('a','c'), ('b', 'd'),('b', 'e'),('c','d'),('c','g'),('e', 'f'),  ('e', 'h')
                   ,('f','h'),('f','g'),('g','h')] ## twin partition

k23=[('1','3'),('1','4'),('1','5'),('2','3'),('2','4'),('2','5')] # k2,3 graph
c6comp=[('1','2'),('1','3'),('1','4'),('2','3'),('2','5'),('3','6'),('4','5'),('4','6'),('5','6')] # c6complement
w45=[('1','2'),('1','5'),('2','3'),('2','6'),('3','4'),('3','6'),('4','5'),('4','6'),('5','6')] # w45

# graph object
g = nx.Graph()
g.add_edges_from(connections)


K23 = nx.Graph()
K23.add_edges_from(k23)

C6co = nx.Graph()
C6co.add_edges_from(c6comp)

w= nx.Graph()
w.add_edges_from(w45)


#nx.draw(g, with_labels=True)
#plt.show()

# time complexity O(n^6)
def recalgo_gut(g):

    for i in range(len(g.nodes()), 1, -1):
    # finding all induced subgraphs of g
        for sub_nodes in itertools.combinations(g.nodes(), i):
            subgraph = g.subgraph(sub_nodes)
            # if the three are isomorphic to an induced subgraph of g
            if (nx.is_isomorphic(subgraph, K23) or nx.is_isomorphic(subgraph, C6co) or nx.is_isomorphic(subgraph, w)):   # if g is not (k23,c6comp,w45)-free
                return False

    # generates clique cutset decomposition tree
    order, new_graph, clique_generator = mcs(g)
    leaves, clique_separator = cliqueCutsets(g, new_graph, clique_generator, order)  # leaves from tree decomposition

    for l in leaves:
        if not is_But(l):   # time complexity O(n^5)
            return False
    return True


print(recalgo_gut(g))

