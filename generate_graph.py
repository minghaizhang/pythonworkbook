#usr/bin/env python
#-*- coding:UTF-8 -*-
#author@blue
#time:2019.07.31

#generate a graph and show 

import numpy as np
import random
import networkx as nx
from IPython.display import Image
import matplotlib.pyplot as plt

# Generate the graph
n = 70
p = 0.2
G_erdos = nx.erdos_renyi_graph(n,p, seed =100)
# Plot the graph
plt.figure(figsize=(12,8))
nx.draw(G_erdos, node_size=10)
fig = plt.gcf()
plt.show()
fig.savefig('a generate graph1.png',dpi=100)

print('that is generate graph and nice')
