import networkx as nx
from copy import deepcopy
from hole import is_hole
from anticomponent import anticomponents




# Defining function for if the graph is basic in Gu
def is_Bu(g):

    node_no = g.number_of_nodes() # gets the number of nodes

    node_deg = [] # stores the degree of all nodes
    for i in g.nodes:
        node_deg.append(g.degree(i))  # getting the degree of all nodes


    if all (k >= node_no - 2 for k in node_deg):

        #getting anticomponents
        a = anticomponents(g)
        acomp_no = len(a)


        if acomp_no == 0:
            print('a')
            return True        # all are trivial anticomponents

        if acomp_no > 0:
            for i in a:
                if nx.number_of_nodes(i) <= 2:

                    return True                    # isomorphic to k2 complement or k1 (i) or (ii)


    elif any (k <= node_no - 3 for k in node_deg):

        u = []
        for i in g.nodes:
            if g.degree(i) == node_no - 1:  # form set of all vertices of degree n-1
                u.append(i)

        print(u)
        v = []
        G1 = deepcopy(g)
        for n in G1.nodes():
            v.append(n)
        if len(u)>0:
            for j in u:
                v.remove(j)

        print(v)

        G2 = g.subgraph(v)

        if is_hole(G2):         # if it is a hole

            if len(G2) >=5:     # if it is a long hole
                return True

        if len(G2) >= 3:   # if it has at least 3 vertices and is a disjoint union of paths
            for c in nx.connected_components(G2):
                n = len(c)
                if n == 1:
                    continue
                if not sorted(dict(nx.subgraph(G2, c).degree()).values()) == [1, 1] + [2] * (n - 2):
                    return False
            return True


    return False


