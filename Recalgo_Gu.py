import networkx as nx
import itertools
import numpy as np
from Bu import is_Bu
from mcs import mcs,cliqueCutsets
from anticomponent import anticomponents


connec1 = [('1', '2'),('1', '3'),('2','3'), ('3', '4'),('3', '7'),('4','5'),('5','6'),
                ('4', '6'),  ('4', '8'),('7','8'), ('7','9'),('8','9')]

connections=[('1','2'),('1','3'),('1','5'),('1','4'),('3','2'),('3','1'),('3','5'),('5','4'),('2','5')]


connec2=[('1', '3'), ('1', '4'),('1','6'), ('2', '3'),('2', '7'),('3','8'),('3','6'),('3', '4'),
        ('4', '5') ,('4','9'),('4','6'),('5','10'),('7','8'),('8','11'),('11','9'),('9','10')] #gu graph

# creating sample graph object

g = nx.Graph()
g.add_edges_from(connec2)



# perform clique cut-set decomposition of graph g and get the tree leaves (L1, L2,...,Lk)

# checking if graph is basic


# check if graph (G) has clique cutset (a clique such that its removal from G disconnects it)
# clique:

def gu_help(g):

    node_no = g.number_of_nodes()
    node_deg: int = []

    for i in g.nodes:
        node_deg.append(g.degree(i))

        if all(deg>= node_no -2 for deg in node_deg):
            acomp = anticomponents(g)  #getting anti components of g
            acomp_no = len(acomp)
            print(acomp_no)

def gu_recog(g):
    order, fillin_graph, clique_gen = mcs(g)  ## get fill-in graph with perfect elimination ordering.
    leaves, clique_sptr = cliqueCutsets(g, fillin_graph, clique_gen, order)
    print(clique_sptr)
    for leaf in leaves:
        if (not gu_help(leaf)):
            return False
    return True




gu_help(g)