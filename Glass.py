class Glasses:
    def __init__(self):
        self.glassesD=self.createGlass()
    def createGlass(self):
        glasses = {}
        with open("glasses.txt") as glass:
            for line in glass:
                (key1, key2, ammount) = line.split()
                glasses[(key1, key2)] = ammount
        return glasses
        glass.close
    def retG(self):
        return (self.glass, self.color, self.ammount)
    def setGlass(self,gName,gColor):
        self.glass = gName
        self.color = gColor
        self.ammount = self.glassesD[(gName, gColor)]
