import networkx as nx
import itertools


# sample graph input
connec1 = [('1', '2'),
                   ('1', '3'),('2','3'), ('3', '4'),('3', '7'),('4','5'),('5','6'),('4', '6'),  ('4', '8'),('7','8'),
                   ('7','9'),('8','9')]

connections=[('1','2'),('1','3'),('1','5'),('1','4'),('3','2'),('3','1'),('3','5'),('5','4'),('2','5')]


connec2=[('1', '3'),
                   ('1', '4'),('1','6'), ('2', '3'),('2', '7'),('3','8'),('3','6'),('3', '4'),  ('4', '5')
                   ,('4','9'),('4','6'),('5','10'),('7','8'),('8','11'),('11','9'),('9','10')]

connec=[('1','2'),('1','4'),('1','5'),('2','4'),('2','3'),('2','7'),('3','8'),('4','5'),('4','6'),
('4','7'),('5','6'),('6','7'),('8','7')]  # sample graph 2

g = nx.Graph()
g.add_edges_from(connec2)




def anticomponents(g):
    node_no: int=0  # vertex counter
    edge_no: int=0  # edge counter
    anticomponent=[]

    for i in range(len(g.nodes()), 1, -1):
        if node_no > i:
            break
        # finding all induced subgraphs
        for sub_nodes in itertools.combinations(g.nodes(), i):
            subgraph = g.subgraph(sub_nodes)

            complement_g = nx.complement(subgraph)  #complement of the subgraph

            if nx.is_connected(complement_g):         #if the complement is connected
                node_no = len(complement_g.nodes())
                if len(complement_g.edges()) > edge_no:
                    edge_no = len(complement_g.edges())
                    anticomponent = []
                    anticomponent.append(complement_g)

                elif len(complement_g.edges()) == edge_no:
                    anticomponent.append(complement_g)
    return anticomponent

#w = anticomponents(g)

#for i in w:
#   print(i.edges())

