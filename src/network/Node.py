import time
import pickle
from network.block import block 
from network.tx import tx
from utils.CallbackChannel import CallbackChannel

class Node:
    #https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
    #Later, we will be passing in a reference to whatever visualization system we will be using, for the Node to interact with.
    #https://bitcoin.stackexchange.com/questions/10479/what-is-the-merkle-root
    #https://medium.com/hackergirl/how-to-calculate-the-hash-of-a-block-in-bitcoin-8f6aebb0dc6d
    #https://medium.facilelogin.com/the-mystery-behind-block-time-63351e35603a
    '''
    Calculating the MERKLE ROOT
    You take each pair of transaction hashes, concatenate them, and hash them twice with SHA-256.
    Keep doing this until you have only one hash left. When there is an odd number of hashes, concatenate the last hash with itself.
    '''
    
    # requires a nonempty blockchain to start, be sure to insert a genesis block when creating 
    # a new node that has no blockchain yet.
    def __init__(self, network, id=-1, reliability = 1.00):
        # We will ignore the version for now.
        self.id = id
        self.reliability = reliability # a reliability metric we can play with later. Not as important with the bitcoin model?
        self.neighbors = [] # This will be a list containing other Node objects.
        self.sNf = {} # This will be a way to pair nodes with measured reliabilities for them (later).
        self.blockchain = [] # List of blocks.
        self.unconfirmed_txs = [] # A list of tx's we accumulate to peruse through for making blocks with.
        self.confirmed_txs = [tx()] # List of tx's we have confirmed and are ready to put into the next block.
        self.block = block()

        self.callbackChannel = CallbackChannel()

        self.network = network
        self.network.connect(self)
        
    def sendTx(self, dest_Node, tx):
        #visualizer.ping from self to dest 
        dest_Node.recvTx(tx) # 

        self.callbackChannel.run('sendTransaction', {
            'node': self,
            'destination': dest_Node,
            'transaction': tx
        })

        return -1

    def recvTx(self, tx): # handle receiving a transaction
        if(tx in self.unconfirmed_txs): # if i've already got the transaction, drop and stop forwarding.
            return 0
        else: # store the transaction and foward it to neighbors
            self.unconfirmed_txs.append(tx)
            for n in self.neighbors:
                self.sendTx(n, tx)

            if len(self.unconfirmed_txs) > 3:
                self.create_block()
            return 1
        return -1

    # Adds a neighbor to this Node.
    # If neighbor is already present, update their "notes".
    # destination: ID of node to add.
    # notes: Block of text describing this node. (optional)
    # Returns nothing.
    def addNeighbor(self, destination, notes = "N/A"):
        self.neighbors.append(destination)

        self.callbackChannel.run('addNeighbor', {
            'destination': destination,
            'notes': notes
        })

    def create_block(self):
        newBlock = block(transactions = self.unconfirmed_txs, prev_block = self.block)
        self.block = newBlock
        self.unconfirmed_txs = []

        self.callbackChannel.run('newBlock', {
            'node': self
        })

        return newBlock
        # We would keep creating new blocks 
        
    # unused in first iteration - security is not priority.
    def verifyTx(self, tx): # verify a tx is valid
        return True
   
    def request_top_block(self, dest_node):
        return dest_node.blockchain[-1] # requires nonempty blockchain
    
    def recv_block(self, src_node, block): # Handle a block that has been received.
        if(block.height <= len(self.blockchain)): # if we get a block we already have
            return -1
        elif(block.height > len(self.blockchain)):
            for i in range(len(self.blockchain), block.height): # for every block of difference between our blockchain
                self.blockchain.append(src_node.blockchain[i])
                # no security or verification of correctness here yet.
                
    def send_block(self, dest_node, block_num): # send a block out to neighbors
        if(block_num <= len(self.blockchain)):
            dest_node.recv_block(self, self.blockchain[block_num])
            return 1
        else:
            return -1
           
    # Requesting blocks should only be done if you receive transactions from other nodes indicating their chain length
    # is greater than yours!
    def request_block(self, dest_node, block_num):
        dest_node.send_block(self, self, block_num)
        return 1
    
    def request_block_range(self, dest_node, block_num_1, block_num_2): # Request a full copy of a range of blocks from another node
        return -1

    def save_blockchain_to_file(self, filename):
        return -1

    def load_blockchain_from_file(self, filename):
        return -1
