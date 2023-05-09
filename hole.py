import networkx as nx

hole = [('5', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5')] # hole graph

#g = nx.Graph()
#g.add_edges_from(hole)


def is_hole(g):     # returns true if graph is a hole and false otherwise
    if len(g) >= 4:
        if nx.is_connected(g):
            deg = []
            for i in g.nodes:
                deg.append(g.degree(i))

            for j in deg:
                if j != 2:
                    return False
                else:
                    return True

    else:
        return False



#l = is_hole(g)
#print(l)