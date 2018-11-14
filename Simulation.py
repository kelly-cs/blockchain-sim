from Network import Network
from Node import Node
from Wallet import Wallet
from Transaction import Transaction

class Simulation:
    def __init__(self):
        self._network = Network()

    # Creates a new, empty node with a 
    # Returns the new node instance.
    def createNode(self, nodeID = None):
        node = Node(self._network, nodeID)
        return node