import uuid

class Node:
    def __init__(self, id, network):
        self._network = network
        self._id = id || uuid.uuid4()

        self._network.connect(self)

        """
        Structure of self._neighbors is as follows:
        {
            [nodeID]: [notes]
        }
        """
        self._neighbors = {}
        self._transactions = []

    def getId(self):
        return self._id

    def recieveTransaction(source, transaction, reliability):
        pass

    def verifyTransaction(source, transaction):
        pass

    def listWallet(source, walletID):
        pass

    def getNeighbors(source):
        pass

    def storeTransaction(transaction):
        for transactionStored in self._transactions:
            if transactionStored == transaction:
                return
        self._transactions.append(transaction)

    def loadTransaction(transaction):
        pass

    def searchTransaction(walletID, first):
        pass

    def sendTransaction(destination, transaction, reliability):
        pass

    # Calls sendTransaction for each transaction in transactionList.
    # destination: ID of node to send.
    # transactionList: Array of Transaction objects (TODO?) to send.
    # Returns nothing.
    # TODO: Reliability is always set to 1. Need to change.
    def sendTransactionList(destination, transactionList):
        for transaction in transactionList:
            self.sendTransaction(destination, transaction, 1)

    # Returns a dict of the connected neighbors and their notes.
    # See __init__ for the structure of this dict.
    def listNeighbors();
        return this._neighbors

    # Adds a neighbor to this Node.
    # If neighbor is already present, update their "notes".
    # destination: ID of node to add.
    # notes: Block of text describing this node. (optional)
    # Returns nothing.
    def addNeighbor(destination, notes = "N/A"):
        self._neighbors[destination] = notes

    # Remove a neighbor from this Node.
    # If neighbor does not exist, ignore it.
    # destination: ID of node to remove.
    # Returns nothing.
    def dropNeighbor(destination):
        del self._neighbors[destination]

