import networkx as nx
import itertools
import matplotlib.pyplot as plt
from copy import deepcopy
from collections import deque

connections1 = [('1', '2'),
                   ('1', '3'),('2','3'), ('3', '4'),('3', '7'),('4','5'),('5','6'),('4', '6'),  ('4', '8'),('7','8'),
                   ('7','9'),('8','9')]

connections=[('1','2'),('1','3'),('1','5'),('1','4'),('3','2'),('3','1'),('3','5'),('5','4'),('2','5')]


connections2=[('1', '3'),
                   ('1', '4'),('1','6'), ('2', '3'),('2', '7'),('3','8'),('3','6'),('3', '4'),  ('4', '5')
                   ,('4','9'),('4','6'),('5','10'),('7','8'),('8','11'),('11','9'),('9','10')]

connec=[('1','2'),('1','4'),('1','5'),('2','4'),('2','3'),('2','7'),('3','8'),('4','5'),('4','6'),
('4','7'),('5','6'),('6','7'),('8','7')]  # gu graph

g = nx.Graph()
g.add_edges_from(connections2)

#nx.draw(g)
#plt.show()





## Begin MCS M algorithm   time complexity is O(nm)
def mcs(g:nx):
    g1 = deepcopy(g)
    nodes = len(g.nodes())
    order = [0]*nodes
    w= {}
    s=-1
    clique_gen = []
    fill_edges = []
    for key in g1.nodes():
        w[key]=0

    for i in range(nodes,0,-1):
        #filtered = filter(lambda value: value !)
        filt_Dict = {key: value for (key, value) in w.items() if key not in order}
        v = max(filt_Dict, key=filt_Dict.get)  ## picked unnumbered max weight vertex

        if w[v]<=s:
            clique_gen.append(v)
        s=w[v]
        reached={}
        for key in g1.nodes():
            if key==v:
                reached[key]=True
            else:
                reached[key]=False

        reach=[None]*nodes
        adj=[]
        adj=list(g1.neighbors(v))
        for key in adj:
            reached[key] = True
            if(reach[w[key]]==None):
                reach[w[key]]=deque([])
            reach[w[key]].append(key)

        for j in range(nodes):
            while reach[j] !=None and len(reach[j])>0:
                u=reach[j][0]
                reach[j].popleft()
                for z in list(g1.neighbors(u)):
                    if not reached[z]:
                        reached[z] = True
                        if w[z] > j:
                            adj.append(z)
                            if (reach[w[z]] == None):
                                reach[w[z]] = deque([])
                            reach[w[z]].append(z)
                        else:
                            reach[j].append(z)
        for u in adj:
            w[u] = w[u] + 1
            fill_edges.append((v, u))
        order[i - 1] = v
        g1.remove_node(v)
    new_graph = nx.Graph(fill_edges)
    return order, new_graph, clique_gen

order,fillin_graph, clique_gen=mcs(g)

print(order)
print(clique_gen)


def cliqueCutsets(g:nx, fillin_graph, clique_gen, order):
    g1 = deepcopy(g)
    h1 = deepcopy(fillin_graph)
    clique_sptr = []
    leafs = []
    for x in order:
        if x in clique_gen:
            separator = list(h1.neighbors(x))
            if g.is_clique(separator):
                clique_sptr.append(separator)
                g1_copy = deepcopy(g1)
                for v in separator:
                    g1_copy.remove_node(v)
                c = list(set(g1_copy.neighbors(x)))  #
                g1_copy.remove_node(x)
                for u in c:
                    nlist = g1_copy.neighbors(u)
                    c = c + list(nlist)
                    g1_copy.remove_node(u)
                c = c + [x]  ### connected component containg x
                del g1_copy
                conn = g1.get_connections(c + separator)  # getting edges for the leafs
                leaf_graph = nx(conn)  ## form leaf graph which does not admit clique-cutset.
                leafs.append(leaf_graph)
                for v in c:
                    g1.remove_node(v)
        h1.remove_node(x)
    leafs.append(g1)
    return leafs, clique_sptr



