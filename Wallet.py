import uuid

class Wallet:
    def __init__(self, id=uuid.uuid4(), coin):
        self._id = id
        self._coin = coin or 0

    def getId(self):
        return self._id

    def changeRSC(self, amt):
        self._coin += amt

    def getRSC(self, amt):
        return self._coin