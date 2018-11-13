class Simulation:
    def __init__(self):
        self._nodeList = []
        self._nodeDict

    # Checks if input is a node id
    # If so, find the corresponding node and return it
    # Otherwise, return the input
    def resolveNodeId(self, node):
        if (type(node) == str)
            return self._nodeDict[node]

        return node1

    # Adds an existing node into the simulation
    # Returns nothing.
    def addNode(self, node):
        self._nodeList.append(node)
        self._nodeDict[node.id] = node

    # Removes a node from the simulation
    # Returns success status
    def removeNode(self, node):
        try:
            node = resolveNodeId(node)
            self._nodeList.remove(node)
            del self._nodeDict[node.id]
            return true
        except(Exception e):
            return false

    # Creates a new, empty node with a 
    # Returns the new node instance.
    def createNode(self, nodeID):
        node = Node(nodeID)
        self.addNode(node)
        return node

    def connectNodes(self, node1, node2):
        node1 = resolveNodeId(node1)
        node2 = resolveNodeId(node2)
        node1.addNeighbor(node2);