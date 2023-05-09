import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
from hole import is_hole
from contains_hole import contains_hole


k23=[('1','3'),('1','4'),('1','5'),('2','3'),('2','4'),('2','5')] # k2,3 graph
c6comp=[('1','2'),('1','3'),('1','4'),('2','3'),('2','5'),('3','6'),('4','5'),('4','6'),('5','6')] # c6bar
w45=[('1','2'),('1','5'),('2','3'),('2','6'),('3','4'),('3','6'),('4','5'),('4','6'),('5','6')] # w45

#g = nx.Graph()
#g.add_edges_from(w45)

#nx.draw(g, with_labels=True)
#plt.show()

# time complexity O(n^5)
def k23Graph(g):

    if nx.is_bipartite(g): # if g is bipartite
        if len(g) == 5:  # if g has 5 nodes
            X, Y = bipartite.sets(g)    # gets nodes from each side of bipartite graph

            for i in X:
                n = g.neighbors(i)
                if set(list(n)) != set(Y):      # if g is complete
                    return False
                else:
                    continue
            if (len(X) == 2 and len(Y) ==3):    # if g is K2,3
                return True
    return False

# time complexity O(n^6)
def C6comp(g):
    if len(g) == 6: # if g has 6 nodes
        comp = nx.complement(g) # get the complement of g
        if is_hole(comp): #if the complement is a hole
            return True

    return False
    
# time complexity O(n^6)
def w45(g):
    if len(g) == 6: # if g has 6 nodes
        if contains_hole(g):  # if g contains a hole
            one_deg=[]
            for i in g.nodes:
                degr = g.degree(i)
                if degr == 4:  # if there is only one node of degree 4
                    one_deg.append(i)

            if len(one_deg) == 1:
                return True
    return False


#print(k23Graph(g))
#print(C6comp(g))
#print(w45(g))