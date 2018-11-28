
class block:
    def __init__(self):
		self.transactions = [] # a list containing transaction objects.
		self.merkle = ""
		self.timestamp = 1 # unix time
		self.difficulty = 1 # difficulty bits
		self.nonce = 1 # nonce for generating the hash
		self.prev_block = "" # hash of the previous block
		self.hash = "" # hash of this block