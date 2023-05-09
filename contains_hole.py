import networkx as nx
import matplotlib.pyplot as plt


contains_hole=[('1','2'),('1','3'),('2','4'),('3','5'),('3','6'),('4','5'),('5','6')]
#g = nx.Graph()
#g.add_edges_from(contains_hole)

#nx.draw(g, with_labels=True)
#plt.show()

not_in_hole = {}
in_path = {}

def process(a, b, c, g):
    in_path[c]=1

    neigh_c =[]
    neigh = g.neighbors(c)
    for n in neigh:
        neigh_c.append(n)

    for d in neigh_c:
        neigh_d = []
        n = g.neighbors(d)
        for i in n:
            neigh_d.append(i)

        if not a in neigh_d and not b in neigh_d: # if d is adjacent to neither a nor b
            if in_path[d]==1:
                return True
            elif not_in_hole[(b,c),d] == 0:
                return process(b,c,d,g)

    in_path[c]=0
    not_in_hole[(a,b),c] = 1
    not_in_hole[(c,b),a] = 1


def contains_hole(g):

    if nx.is_connected(g): # check if the graph is connected

        for v in g.nodes:
            for e in g.edges:
                not_in_hole[e, v] = 0
                not_in_hole[(e[1], e[0]), v] = 0
            in_path[v] = 0

        for u in g.nodes:
            in_path[u] = 1
            ne = [] # store neighbours of u
            n = g.neighbors(u)
            for neigh in n:
                ne.append(neigh)        # get neighbours of node u
            for vw in g.edges():
                if (vw[0] in ne and not vw[1] in ne and not_in_hole[(u, vw[0]), vw[1]] == 0):
                    in_path[vw[0]] = 1
                    if process(u, vw[0], vw[1], g) == True:
                        return True
                    in_path[vw[0]] = 0
            in_path[u] = 0
        return False





#l = contains_hole(g)
#print(l)