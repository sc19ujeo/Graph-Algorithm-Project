import networkx as nx
import matplotlib.pyplot as plt
from hole import is_hole
from copy import deepcopy


ring=[('1','2'),('1','5'),('2','3'),('3','4'),('4','5'),('1.','1'),('1.','5'),('1.','2'),('2.','2'),
        ('2.','1'), ('2.','3'),('2.','3.'),('3.','3'),('3.','2'),('3.','4')]  # ring graph



# creating sample graph object

#g = nx.Graph()
#g.add_edges_from(ring)

#nx.draw(g, with_labels=True)
#plt.show()

# time complexity: O(n)
def is_ring(g):

        Xlist = []

        if not nx.is_connected(g):    # if the graph isnt connected
                return (False, 0)

        if nx.is_chordal(g):           # if the graph is chordal
                return (False, 0)


        node_deg = []     # list of degree of all nodes
        max_deg_node = []  # list for node with the highest degree
        max_deg = 0   #highest degree
        for i in g.nodes():
                node_deg.append(g.degree(i))
                if len(node_deg) > 1:
                        j = len(node_deg)-1
                        if node_deg[j] > node_deg[j-1]:
                                if max_deg < node_deg[j]:
                                        max_deg = node_deg[j]
                                        max_deg_node.clear()
                                        max_deg_node.append(i)


        X1 = []

        ngx = []  # Ng[x] (set of neighbours of vertex x and vertex x itself)
        for x in max_deg_node:
                ngx.append(x)
                b = g.neighbors(x)
                for j in b:
                        ngx.append(j)



        for y in g.nodes():
                ngy = []  # Ng[y] (set of neighbours of vertex y and vertex y itself)
                ngy.append(y)
                n = g.neighbors(y)
                for j in n:
                        ngy.append(j)

                if(set(ngy).issubset(set(ngx))):  # if Ng[y] is a subset of Ng[x]
                        X1.append(y)
                ngy.clear()




        n1 = len(X1)

        # sort X1 from max to min degree
        x1deg = []
        max_deg1 = 0
        for i in X1:
                x1deg.append(g.degree(i))

        if n1>1:
                for j in range(1, n1):

                        if x1deg[j] > x1deg[j - 1]:


                                if x1deg[j] > max_deg1:

                                        max_deg1 = x1deg[j]
                                        elem = X1.pop(j)
                                        X1.insert(0, elem)
                                else:
                                        el = X1.pop(j - 1)
                                        X1.insert(j, el)

        # check whether the set containing the neighbours of each node & the node itself is a
        # subset of the set containing the neighbours of its previous node & the previous node
        # itself in X1.
        nx1s = [] # Ng[u]

        for i in X1:
                nx1 = []  # buffer for storing neigbors of a node in X1
                nx1.append(i)
                b = g.neighbors(i)

                for j in b:
                        nx1.append(j)
                nx1s.append(nx1)


        if n1 > 0:
                for j in range(1, n1):

                        if not (set(nx1s[j]).issubset(set(nx1s[j-1]))):
                                return (False, 0)


        if n1 > 0:
                Xlist.append(X1)


        l = deepcopy(g)   # copy of g used to compute G / X1
        for i in X1:
                l.remove_node(i)

        subnodes = []
        for i in l.nodes:
                subnodes.append(i)
        sub = g.subgraph(subnodes)    # subgraph of g induced by X1

        if not nx.is_chordal(sub):   # if G / X1 is not chordal then g is not a ring
                return (False, 0)


        neighx1_0 = [] #Ng(u1) (neighbors of first node in X1)
        b = g.neighbors(X1[0])
        for j in b:
                neighx1_0.append(j)
        findc = neighx1_0.copy()


        for i in X1:
                if i in neighx1_0:
                        findc.remove(i)

        c = g.subgraph(findc)
        components = nx.connected_components(c)  # component of G[Ng(u1) / X1]


        # X2 = vertex set of a component of G[Ng(u1) / X1]
        X2 = []
        comp = list(components)
        for i in comp[0]:
                X2.append(i)     # appends nodes from each component


        n2 = len(X2)
        x2deg = []

        for i in X2:
                x2deg.append(g.degree(i))   # gets the degree of each node in X2

        max_deg2 = 0
        # sorts X2 by degree size from max to min
        if n2 > 1:
                for j in range(1, n2):

                        if x2deg[j] > x2deg[j - 1]:
                                if x2deg[j] > max_deg2:
                                        max_deg2 = x2deg[j]
                                        elem = X2.pop(j)
                                        X2.insert(0,elem)
                                else:
                                        el = X2.pop(j - 1)
                                        X2.insert(j, el)


        # check whether the set containing the neighbours of each node & the node itself is a
        # subset of the set containing the neighbours of its previous node & the previous node
        # itself in X2.
        nx2s = []  # Ng[u2]

        for i in X2:
                nx2 = [] # buffer for storing neigbors of a node in X2
                nx2.append(i)
                b = g.neighbors(i)

                for j in b:
                        nx2.append(j)
                nx2s.append(nx2)


        if n2 > 1:
                for i in range(1, n2, 1):
                        if not (set(nx2s[i]).issubset(set(nx2s[i-1]))):
                                print('a')
                                return (False, 0)



        if n2>0:
                Xlist.append(X2)


        k = len(Xlist)


# STEP 2


        while True:

                neighxk_1 = []   # to store neighbours of first node of Xk



                b = g.neighbors(Xlist[k-1][0])
                for i in b:
                        neighxk_1.append(i)


                unionofxlist = []
                for i in Xlist:
                        for j in i:
                                unionofxlist.append(j)



                Xk1 = neighxk_1.copy()
                for i in unionofxlist:
                        if i in neighxk_1:
                                Xk1.remove(i)


                nk1 = len(Xk1)

                if nk1 == 0:

        # STEP 3
                        n = []
                        if k<=3:

                                return (False, 0)

                        for i in g.nodes():
                                n.append(i)

                        if set(unionofxlist).issubset(set(n)):  #if X1 u X2 u....u Xk is a subset of
                                                                # set of vertices in g
                                unionofxlist.sort()
                                n.sort()

                                if unionofxlist != n:

                                        return (False, 0)

                        u1v = [] # to store first vertices of each partition
                        for i in range(0, k):    # gets first nodes from X1....Xk
                                u1v.append(Xlist[i][0])
                        uv = g.subgraph(u1v)
                        if is_hole(uv):
                                return True, k, Xlist       # returns true, the ring length and the good partition
                        else:
                                return (False,0)

                # ordering Xk+1 based on degree of each node from max to min
                xk1deg = []
                for i in Xk1:
                        xk1deg.append(g.degree(i))

                max_degk1 = 0
                if nk1 > 1:
                        for j in range(1, nk1):

                                if xk1deg[j] > xk1deg[j - 1]:
                                        if xk1deg[j] > max_degk1:
                                                max_degk1 = xk1deg[j]
                                                elem = Xk1.pop(j)
                                                Xk1.insert(0, elem)
                                        else:
                                                el = Xk1.pop(j - 1)
                                                Xk1.insert(j, el)


                # check whether the set containing the neighbours of each node & the node itself is a
                # subset of the set containing the neighbours of its previous node & the previous node
                # itself in Xk+1.

                nxk1s = []
                nxk1 = []
                for i in Xk1:
                        nxk1.append(i)
                        b = g.neighbors(i)
                        for j in b:
                                nxk1.append(j)
                        nxk1s.append(nxk1)

                        if len(nxk1s) > 1:
                                j = len(nxk1s) - 1
                                if not (set(nxk1s[j]).issubset(set(nxk1s[j - 1]))):
                                        return (False,0)
                        nxk1.clear()

                if nk1 > 0:
                        Xlist.append(Xk1)

                k+=1        # update k


#l = is_ring(g)
#print(l)