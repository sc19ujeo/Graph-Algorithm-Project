import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy




def twin_classes(g):

    P = [] # for storing twin classes

    # checking for truwe twins
    # getting set of neighbours of a vertex u and vertex u
    for u in g.nodes:
        ngu = []
        ngu.append(u)
        n = g.neighbors(u)
        for i in n:
            ngu.append(i)

        nou = deepcopy(g)
        nou.remove_node(u)      # removing node u from g

        for v in nou.nodes:
            ngv = []
            ngv.append(v)
            n = g.neighbors(v)
            for i in n:
                ngv.append(i)           # getting set of neighbours of a vertex u and vertex u


            if  set(ngu) == set(ngv):
                tt = []
                tt.append(u)
                tt.append(v)
                P.append(tt)

                # to remove true twins which have already been in the list
                for i in P:
                    ttr = P.copy()
                    ttr.remove(i)
                    for j in ttr:
                        if set(i) == set(j):
                            P.remove(j)


    def adjacent(B, C):                # condition for if two twin classes B and C are adjacent
        b = list(B)
        c = list(C)

        ttneigh = [] # store neighbours of nodes in b
        ttneigh2 = []

        for k in b[0]:
            ne = g.neighbors(k)
            for l in ne:
                ttneigh.append(l)

        for k in b[1]:
            n = g.neighbors(k)
            for l in n:
                ttneigh2.append(l)


        if set(c).issubset(set(ttneigh)) and set(c).issubset(set(ttneigh2)):   # if B is complete to C

            ttneigh3 = []
            ttneigh4 = []

            for j in c[0]:
                n = g.neighbors(j)
                for k in n:
                    ttneigh3.append(k)

            for j in c[1]:
                n = g.neighbors(j)
                for k in n:
                    ttneigh4.append(k)


            if set(b).issubset(set(ttneigh3)) and set(b).issubset(set(ttneigh4)): # if C is complete to B
                return True

            return False


        return False

    gp = nx.quotient_graph(g, P, edge_relation=adjacent)

    return gp


#l = twin_classes(g)
#print(l)