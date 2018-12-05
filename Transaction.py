import uuid

class AdjustmentTotalError(Exception):
    pass

class Transaction:
    def __init__(self, adjustmentDict = {}, id = None):
        self.id = id or uuid.uuid4()
        self._adjustmentDict = {}
        self.addAdjustments(adjustmentDict)

    def verifyAdjustments(self):
        total = 0
        for key in self._adjustmentDict.keys():
            total += self._adjustmentDict[key]
        
        if total != 0:
            raise AdjustmentTotalError

    def addAdjustment(self, walletID, adjustment):
        self._adjustmentDict[walletID] = adjustment

    def addAdjustments(self, adjustmentDict):
        # Shallow merge both dicts
        self._adjustmentDict = {**self._adjustmentDict, **adjustmentDict}
    
    def getAdjustments(self):
        return {**self._adjustmentDict}

    # Checks if another transaction is equal to this one.
    # Overrides the equals operator.
    # other: Another Transaction object.
    def __eq__(self, other):
        return self.id == other.id
        
    def containsWallet(self, walletID):
        return walletID in self._adjustmentDict.keys()


