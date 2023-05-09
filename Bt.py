import networkx as nx
from hole import is_hole
from twin_class import twin_classes
from ring import is_ring




def is_Bt(g):

    hp = twin_classes(g) # returns quotient graph
    n = nx.number_of_nodes(hp)
    if n == 1:    # if quotient graph is a one vertex graph   runtime: O(1)
        return True

    if n > 1:
        if nx.number_of_edges(hp) > 0:
            if not is_ring(hp):     # if quotient graph is not a ring        runtime: O(nxn)
                return False

            cmpl = nx.complement(hp)
            if n != 7 or not is_hole(cmpl):  # if quotient graph is not a 7-anti hole   runtime: O(n)
                    return False


    return True

