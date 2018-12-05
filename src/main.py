'''
Simulating the blockchain environment: 
This program will create x amount of nodes, and begin feeding transactions to nodes in the network
at random.

First iteration, for demo, will not have the bells and whistles (security, meaningful proof of work)

'''
# Our Libraries #
from network.tx import tx
from network.block import block
from network.Node import Node
from network.network import Network
from gui.visualize import Visualizer
import random
import time

if __name__ == "__main__":
    print("Beginning Simulation")

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
                if len(node1.neighbors) == 0:
                    continue
                node2 = node1.neighbors[random.randint(0, len(node1.neighbors) - 1)]
                if node1 is node2:
                    continue
                node1.sendTx(node2, tx())
                timer = 30
                break
        timer -= 1

        vis.tick()
        time.sleep(1.0 / 60.0)