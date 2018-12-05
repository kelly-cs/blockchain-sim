from network.tx import tx
class block:
    def __init__(self, transactions = [], prev_block = None):
        self.transactions = [] # a list containing transaction objects.
        self.merkle = ""
        self.timestamp = 1 # unix time
        self.difficulty = 1 # difficulty bits
        self.nonce = 1 # nonce for generating the hash
        self.prev_block = "" # hash of the previous block
        self.hash = "" # hash of this block
        self.height = 0 # height of this block in chain
        if prev_block:
            self.height = prev_block.height + 1

    def calculateScore(self):
        return self.height

    # calculate the merkle root of all the transactions in the block
    def calculate_merkle(self, tx_list):
        return -1

    def confirm_signature(self, tx):
        return -1
