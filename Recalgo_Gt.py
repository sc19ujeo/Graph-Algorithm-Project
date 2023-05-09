import networkx as nx
import matplotlib.pyplot as plt
from Bt import is_Bt
from mcs import mcs,cliqueCutsets

gt =[('1', '2'), ('7','8'), ('5', '6'), ('1', '4'), ('1','3'), ('2', '4'), ('2', '5'), ('3','4'), ('3','7'),
         ('5', '8'), ('6','8'), ('6','7')] # gt graph

gt2=[('1', '2'),('2', '3'), ('3','4'),('1','3'),('1','5'),('2', '6'),('1', '4'),('3','5'),('4', '5')
    ,('4','7'),('5','7'),('6','8'),('8','7'),('9','6'),('i','8'),('9','7')] ## not gt graph

g = nx.Graph()
g.add_edges_from(gt2)

#nx.draw(g, with_labels=True)
#plt.show()


def recalgo_gt(g):
    order, new_graph, clique_generator = mcs(g)
    leaves, clique_separator = cliqueCutsets(g, new_graph, clique_generator, order)  # leaves from tree decompostion
    for l in leaves:
        if not (is_Bt(l)):   # checking if any of the decompostion tree leaves are not basic (Bt)
            return False
    return True

j = recalgo_gt(g)
print(j)