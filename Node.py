import uuid

class Node:
    def __init__(self, network, id):
        self._network = network
        self._id = id or str(uuid.uuid4())

        self._network.connect(self)

        
        # Structure of self._neighbors is as follows:
        # {
        #     [nodeID]: [notes]
        # }
        self._neighbors = {}
        self._transactions = []

    # Returns the node id.
    # Direct access to _id is discouraged as it could be modified.
    # Unfortunately, I don't believe Python has a way to declare private members.
    def getID(self):
        return self._id

    def recieveTransaction(self, source, transaction, reliability):
        pass

    def verifyTransaction(self, source, transaction):
        pass

    def listWallet(self, source, walletID):
        pass

    # It is not defined at all what this is supposed to do. Supposed to be like sendTransaction? (TODO)
    def sendNeighbor(self, destination, neighbor, notes = ""):
        pass


    def getNeighbors(self, source):
        pass

    # Stores a transaction.
    # If transaction is already stored, ignore it.
    # transaction: Transaction object.
    # Returns nothing.
    def storeTransaction(self, transaction):
        for transactionStored in self._transactions:
            if transactionStored == transaction:
                return
        self._transactions.append(transaction)

    # Checks if a transaction is stored locally.
    # transaction: Transaction object. Does not need to be the same instance as
    #   the local one, but must have the same adjustments.
    # Returns the local Transaction object found.
    def loadTransaction(self, transaction):
        for transactionLocal in self._transactions:
            if transactionLocal == transaction:
                return transactionLocal

    # Search for transactions associated with a certain wallet
    # walletID: ID of Wallet
    # first (optional): Which transaction to start with? Honestly I have no idea what he means here (TODO)
    # Returns the list of transactions and their associated reliabilities (which is always 1 for some reason??)
    # Format is as follows:
    # {
    #   transaction: [transaction object]
    #   reliability: 1   
    # }
    def searchTransactions(self, walletID, first):
        transactionList = []

        for transaction in self._transactions:
            if not transaction.containsWallet(walletID):
                continue
            
            transactionList.append({
                transaction: transaction
                reliability: 1
            })

        return transactionList

    # Sends a transaction to another node
    # destination: ID of node to send to.
    # transaction: Transaction object.
    # reliability: Probability the transaction will later be acknowledged
    def sendTransaction(self, destination, transaction, reliability):
        destNode = self._network.findNode(destination)
        destNode.storeTransaction(transaction)

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

