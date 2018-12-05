from utils.CallbackChannel import CallbackChannel

class Network:
    def __init__(self):
        self._nodeList = []
        self._nodeDict = {}
        self.callbackChannel = CallbackChannel()

    # Checks if input is a node id
    # If so, find the corresponding node and return it
    # Otherwise, return the input
    def findNode(self, node):
        if (type(node) == str):
            return self._nodeDict[node]
        return node

    # Adds an existing node into the network
    # Returns nothing.
    def connect(self, node):
        self._nodeList.append(node)
        self._nodeDict[node.id] = node

        self.callbackChannel.run('connect', {
            'node': node
        })

    # Removes a node from the network
    # Returns success status
    def disconnect(self, node):
        try:
            node = resolveNodeId(node)
            self._nodeList.remove(node)
            del self._nodeDict[node.id]
            return true
        except(Exception):
            return false

        self.callbackChannel.run('disconnect', {
            'node': node
        })