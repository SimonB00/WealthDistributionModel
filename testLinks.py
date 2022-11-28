import matplotlib.pyplot as plt
import numpy as np
import network as n

net = n.network(5,50,50)
adjacency = net.getAdjacency()
net.createLinks(4)

n = 10**5
for i in range(n):
    matrix_el = np.random.choice(list(net.getAdjacency().keys()))
    net.evolveFixed(matrix_el)
print(net.getPoors())

plt.hist(net.getPoors(),bins=500)
plt.show()
plt.hist(net.getPlayers())
plt.show()
