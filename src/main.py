'''
Simulating the blockchain environment: 
This program will create x amount of nodes, and begin feeding transactions to nodes in the network
at random.

First iteration, for demo, will not have the bells and whistles (security, meaningful proof of work)

'''
# Our Libraries #
from network.tx import tx
from network.block import block
from network.node import node
import security
import gui.visualize
from random import randint
#################

import pickle #rick


if __name__ == "__main__":
    print("Beginning Simulation")
    allNodes = [] # List containing all nodes
    amt_of_neighbors = 4 # amt of neighbors for each node
    amt_of_nodes = 400 # amt of unique nodes to create
    
    for i in range(amt_of_nodes):
        new_node = node(id=i) # construct a new node
        allNodes.append(new_node) # append this node to a list containing all nodes
    
    for node in allNodes:
        for neighbor in range(amt_of_neighbors):
            node.neighbors.append(allNodes[randint(0,amt_of_nodes-1)]) # add random neighbors to the node.
   
    
    print("Success.")
    #while True:
        # Let's feed transactions to the network. We will select random nodes and submit
        # transactions to each