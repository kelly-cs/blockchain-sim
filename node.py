
class node:
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
	#
	
    def __init__(self):#Initializer
		# We will ignore the version for now.
        self.id = id  
        self.reliability = reliability # a reliability metric we can play with later. Not as important with the bitcoin model?
        self.neighbors = [] # This will be a list containing other Node objects.
        self.sNf = {} # This will be a way to pair nodes with measured reliabilities for them (later).
        self.blockchain = [] # List of blocks.
		self.unconfirmed_txs = [] # A list of tx's we accumulate to peruse through for making blocks with.
		
	def sendTx(self, dest_Node):
		return -1
	
	def recvTx(self, tx): # handle receiving a transaction
		return -1
	
	def verifyTx(self, tx): # verify a tx is valid
		return -1
	
	
	# Requesting blocks should only be done if you receive transactions from other nodes indicating their chain length
	# is greater than yours!
	def request_block(self, dest_Node, block_num): # Request a full copy of a block's contents
		return -1
	
	def request_block_range(self, dest_node, block_num_1, block_num_2): # Request a full copy of a range of blocks from another node
		return -1
	
	def save_blockchain_to_file(self, filename):
		return -1
	
	def load_blockchain_from_file(self, filename):
		return -1