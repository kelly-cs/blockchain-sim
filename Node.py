import uuid

class Node:
    def __init__(self, network, id):
        self._network = network
        self._id = id or str(uuid.uuid4())

        self._network.connect(self)

        """
        Structure of self._neighbors is as follows:
        {
            [nodeID]: [notes]
        }
        """
        self._neighbors = {}
        self._transactions = []

    def getID(self):
        return self._id

    def recieveTransaction(self, source, transaction, reliability):
        pass

    def verifyTransaction(self, source, transaction):
        pass

    def listWallet(self, source, walletID):
        pass

    def getNeighbors(self, source):
        pass

    def storeTransaction(self, transaction):
        for transactionStored in self._transactions:
            if transactionStored == transaction:
                return
        self._transactions.append(transaction)

    def loadTransaction(self, transaction):
        pass

    def searchTransaction(self, walletID, first):
        pass

    def sendTransaction(self, destination, transaction, reliability):
        pass

    # Calls sendTransaction for each transaction in transactionList.
    # destination: ID of node to send.
    # transactionList: Array of Transaction objects (TODO?) to send.
    # Returns nothing.
    # TODO: Reliability is always set to 1. Need to change.
    def sendTransactionList(self, destination, transactionList):
        for transaction in transactionList:
            self.sendTransaction(destination, transaction, 1)

    # Returns a dict of the connected neighbors and their notes.
    # See __init__ for the structure of this dict.
    def listNeighbors(self):
        return this._neighbors

    # Adds a neighbor to this Node.
    # If neighbor is already present, update their "notes".
    # destination: ID of node to add.
    # notes: Block of text describing this node. (optional)
    # Returns nothing.
    def addNeighbor(self, destination, notes = "N/A"):
        self._neighbors[destination] = notes

    # Remove a neighbor from this Node.
    # If neighbor does not exist, ignore it.
    # destination: ID of node to remove.
    # Returns nothing.
    def dropNeighbor(self, destination):
        del self._neighbors[destination]

