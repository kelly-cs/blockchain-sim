import time
import random

from Network import Network
from Node import Node
from Visualizer import Visualizer
from Transaction import Transaction

network = Network()
nodes = network._nodeList
vis = Visualizer(network)

for i in range(0, 50):
    node = Node(network)

for i in range(0, 100):
    node1 = nodes[random.randint(0, len(nodes) - 1)] 
    node2 = nodes[random.randint(0, len(nodes) - 1)] 
    node1.addNeighbor(node2, 'test')

timer = 0
while 1:
    if timer == 0:
        while True:
            node1 = nodes[random.randint(0, len(nodes) - 1)]
            node1Neighbors = list(node1.neighbors.keys())        
            if len(node1Neighbors) == 0:
                continue
            node2 = node1Neighbors[random.randint(0, len(node1Neighbors) - 1)]
            if node1 is node2:
                continue
            node1.sendTransaction(node2.getID(), Transaction(), 1)
            timer = 5
            break
    timer -= 1

    vis.tick()
    time.sleep(1.0 / 60.0)