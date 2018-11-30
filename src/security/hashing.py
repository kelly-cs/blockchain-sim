# This must be imported by a main function that has node, block, tx imported to function.
# https://bitcoin.stackexchange.com/questions/10479/what-is-the-merkle-root
# https://medium.com/hackergirl/how-to-calculate-the-hash-of-a-block-in-bitcoin-8f6aebb0dc6d

def calculate_tx_hash(tx):
	# calculate the hash of this transaction, given its various stored variables.
	return -1

def calculate_block_hash(block):
	# calculate the hash of the entire block
	return -1

def calculate_merkle(block):
	# given a block, calculate the merkle root of all of its stored transactions.
	return -1

# will take in a tx and return whether or not it is signed by the sender's private key.
def confirm_tx_signature(tx):
	return -1

def confirm_block_hash(block):
	return -1