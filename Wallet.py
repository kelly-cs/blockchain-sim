import uuid

class Wallet:
    def __init__(self, id, rsc):
        self._id = id || uuid.uuid4()
        self._rsc = rsc || 0

    def getId(self):
        return self._id

    def changeRSC(self, amt):
        self._rsc += amt

    def getRSC(self, amt):
        return self._rsc