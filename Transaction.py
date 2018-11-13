class AdjustmentTotalError(Exception):
    pass

class Transaction:
    def __init__(self, adjustmentDict):
        self._adjustmentDict = {}
        self.addAdjustments(adjustmentDict)

    def verifyAdjustments(self):
        total = 0
        for key in self._adjustmentDict.keys():
            total += self._adjustmentDict[key]
        
        if total != 0:
            raise AdjustmentTotalError

    def addAdjustment(walletID, adjustment):
        self._adjustmentDict[walletID] = adjustment

    def addAdjustments(adjustmentDict):
        # Shallow merge both dicts
        self._adjustmentDict = {**self._adjustmentDict, **adjustmentDict}
    