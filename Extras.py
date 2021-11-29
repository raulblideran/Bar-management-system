class Extras:
    def __init__(self):
        self.extrasD=self.createExtras()
    def createExtras(self):
        extras = {}
        with open("extras.txt") as extra:
            for line in extra:
                if not line == "":
                    (key1, key2, quantityE, priceE) = line.split()
                    extras[(key1, key2)] = quantityE, priceE
        return extras
        extra.close()
    def retExtr(self):
        return (self.extra, self.flavour, self.quantityE, self.priceE)
    def setExtra(self, eName, eFlavour):
        self.extra = eName
        self.flavour = eFlavour
        self.quantityE = self.extrasD[(eName, eFlavour)][0]
        self.priceE = self.extrasD[(eName, eFlavour)][1]