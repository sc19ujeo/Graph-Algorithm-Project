import networkx as nx
import itertools
# from mcs import mcs,cliqueCutsets
from anticomponent import anticomponents

# sample graph input
connec1= [('1', '2'),
                   ('1', '3'),('2','3'), ('3', '4'),('3', '7'),('4','5'),('5','6'),('4', '6'),  ('4', '8'),('7','8'),
                   ('7','9'),('8','9')]

connections= [('1','2'),('1','3'),('1','5'),('1','4'),('3','2'),('3','1'),('3','5'),('5','4'),('2','5')]


connec2=[('1', '3'),
                   ('1', '4'),('1','6'), ('2', '3'),('2', '7'),('3','8'),('3','6'),('3', '4'),  ('4', '5')
                   ,('4','9'),('4','6'),('5','10'),('7','8'),('8','11'),('11','9'),('9','10')]

connec=[('1','2'),('1','4'),('1','5'),('2','4'),('2','3'),('2','7'),('3','8'),('4','5'),('4','6'),
('4','7'),('5','6'),('6','7'),('8','7')]  # gu graph

g = nx.Graph()
g.add_edges_from(connec2)

# Defining function for if the graph is basic in Gu
def is_Bu(g):

    # getting all the anti-components
    anticomp = anticomponents(g)

    if len(anticomp) < 1:
        return True


    if len(anticomp) == 1:
        # if anti-component is non-trivial and if non trivial anti-component is a long hole
        if len(anticomp[0].nodes()) >= 5 and all(anticomp[0].degree(deg) == 2 for deg in anticomp[0].nodes()):
            return True

    # if L has more than one anti-component
    if len(anticomp) > 1:
        for i in range(0, len(anticomp)-1, 1):

            # if anti-components are non-trivial
            if len(anticomp[i].nodes()) >= 5:

                # if non trivial anti-components are isomorphic to k2 complement
                if len(anticomp[i].nodes()) == 2 and len(anticomp[i].edges()) == 0:
                    return True

    else:
        return False


#l = is_Bu(g)
#print(l)