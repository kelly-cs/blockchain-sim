
class tx:
	def __init__(self):
		self.sender = "" # wallet address of the sender
		self.receiver = "" # wallet address of the receiver
		self.amt = 0.00 # amt of currency to send
		self.fee = 0.00 # amt of extra fee added for the miner
		self.hash = "" # hash of the sender, receiver, and amt before signing.
		self.signed_hash = "" # signed hash of this transaction, to be cross-referenced with the sending address for validity.
		
	# will take in a tx and return whether or not it is signed by the sender's private key.
    def confirm_signature(self, tx):
        return -1