# Class for a pub-sub style channel
class CallbackChannel:
    def clear(self, tag = None):
        if tag is not None:
            for key in self.tags[tag].keys():
                self.remove(key)
        else:
            self.callbacks = dict()
            self.tags = dict()
            self.callbackCtr = 0

    def __init__(self):
        self.clear()

    def add(self, func, tag = None, countMax = -1):
        if countMax == 0:
            return

        callback = {
            'func': func,
            'tag': tag,
            'countMax': countMax,
            'countCurrent': 0
        }

        if countMax > 0:
            callback['countCurrent'] = 0
        
        self.callbacks[self.callbackCtr] = callback
        
        if tag is not None:
            if tag not in self.tags.keys():
                self.tags[tag] = dict()

            self.tags[tag][self.callbackCtr] = callback
        
        self.callbackCtr += 1
        return self.callbackCtr

    def remove(self, key):
        if key not in self.callbacks.keys():
            return

        tag = self.callbacks[key]['tag']

        # if (typeof tag != "undefined") {
        del self.tags[tag][key]
        if len(self.tags[tag].keys()) == 0:
            del self.tags[tag]

        del self.callbacks[key]

    def run(self, tag = None, data = None):
        tagDict = None
        if tag is None:
            tagDict = self.callbacks
        else:
            if tag not in self.tags.keys():
                return
            tagDict = self.tags[tag]

        #if (typeof tagDict == "undefined") return;

        # If key list is not pulled out first you will get:
        # RuntimeError: dictionary changed size during iteration
        keyList = list(tagDict.keys())
        for key in keyList:
            callback = self.callbacks[key]
            callback['func'](data)
            if callback['countMax'] == -1:
                continue
            callback['countCurrent'] += 1
            # if (typeof callback.countMax != "undefined") {
            if callback['countCurrent'] >= callback['countMax']:
                self.remove(key)

