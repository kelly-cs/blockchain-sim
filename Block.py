import uuid
import time

class Block:
	def __init__(self, transactions = None, blockPrev = None):
		self.transactions = transactions or [] # a list containing transaction objects.
		self.merkle = ""
		self.timestamp = time.time() # unix time
		self.difficulty = 1 # difficulty bits
		self.nonce = 1 # nonce for generating the hash
		self.blockPrev = blockPrev # previous block
		self.hash = self.generateHash() # hash of this block (fake atm)
		
	def generateHash(self):
		return uuid.uuid4()

	def calculateScore(self):
		return len(self.transactions)

	# calculate the merkle root of all the transactions in the block
	def calculateMerkle(self, tx_list):
		return -1
	
	def confirmSignature(self, tx):
		return -1