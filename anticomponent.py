import networkx as nx
import itertools
import matplotlib.pyplot as plt


# sample graph

antic_test=[('1', '3'), ('9','10'), ('1', '4'),('1','6'), ('2', '3') ,('11','9'),('4', '5'),('3', '4'),('4','9'),
            ('4','6'), ('3','8'), ('5','10'),('8','11'),('7','8')]


g = nx.Graph()
g.add_edges_from(antic_test)

# nx.draw(g, with_labels=True)
# plt.show()



def anticomponents(g):
    node_no =0  # vertex counter
    edge_no =0  # edge counter
    anticomponent=[]



    for i in range(len(g.nodes()), 1, -1):

        if node_no > i:  # checking if it is maximal
            break
        # finding all induced subgraphs
        for sub_nodes in itertools.combinations(g.nodes(), i):

            subgraph = g.subgraph(sub_nodes)

            complement_g = nx.complement(subgraph)    # complement of the subgraph

            if nx.is_connected(complement_g):         # if the complement is connected (anticonnected)
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
#  print(i.nodes())

