import networkx as nx
import matplotlib.pyplot as plt
from Bu import is_Bu
from mcs import mcs,cliqueCutsets

gu=[('2','5'),('1','3'),('1','5'),('1','4'),('1','2'),('3','1'),('3','2'),('3','5'),('5','4')] #gu graph

gu2=[('1', '3'), ('7','8'), ('1','6'),('11','9'),('1', '4'),('2', '3'),('2', '7'),('3','8'),('3','6'),('3', '4'),
        ('4', '5') ,('4','9'),('9','10'), ('4','6'),('5','10'),('8','11')] #gu2 graph


# creating sample graph object

g = nx.Graph()
g.add_edges_from(connec)
#nx.draw(g)
#plt.show()


def recalgo_gu(g):
    order, fillin_graph, clique_generator = mcs(g)
    leaves, clique_separator = cliqueCutsets(g, fillin_graph, clique_generator, order) # leaves from tree decompostion
    print(clique_separator) # family of induced subgraphs of G

    for l in leaves:
        if (not is_Bu(l)):   # checking if any of the decompostion tree leaves are not basic (Bu)
            return False
    return True


j = recalgo_gu(g)
print(j)