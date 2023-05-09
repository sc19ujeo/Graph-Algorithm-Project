import networkx as nx
import matplotlib.pyplot as plt
from ring import is_ring
from contains_hole import contains_hole
from networkx.algorithms import approximation as approx


# time complexity: O(n^6)
def is_But(g):

      antic = [] # for storing anticomponents

      cmpl = nx.complement(g) # complement of g

      compon= nx.connected_components(cmpl) #components of complement


      for i in compon:
            ind = g.subgraph(i)
            cmpl2 = nx.complement(ind)   #complement of each component
            antic.append(cmpl2)


      for j in antic:

            l = is_ring(j)

            if l[0] == True:      #if it's a ring
                  if l[1] >= 5:       # if it's a long ring

                        return True

            ss =approx.maximum_independent_set(j)
            if len(ss)<=2: # if stable set size is less than or equal to 2

                  return True

            if contains_hole(j): # if it contains no long hole
                  if not len(j) >=5:
                        return True
      return False



#l = is_But(g)
#print(l)