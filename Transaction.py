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

    def addAdjustment(self, walletID, adjustment):
        self._adjustmentDict[walletID] = adjustment

    def addAdjustments(self, adjustmentDict):
        # Shallow merge both dicts
        self._adjustmentDict = {**self._adjustmentDict, **adjustmentDict}
    
    def getAdjustments(self):
        return {**self._adjustmentDict}

    # Checks if another transaction is equal to this one.
    # other: Another Transaction object.
    def __eq__(self, other):
        if other == self:
            return true

        adjustmentsSelf = self._adjustmentDict
        adjustmentsOther = other.getAdjustments() 
        for key in adjustmentsSelf.keys():
            if key not in adjustmentsOther.keys():
                return false
            if adjustmentsSelf[key] != adjustmentsOther[key]:
                return false
        
        return true