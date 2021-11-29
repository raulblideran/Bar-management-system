class Drinks(object):
    def __init__(self):
        self.drinksD = self.createDrinks()
    def createDrinks(self):
        drinks = {}
        with open("Drinks.txt") as text:
            for line in text:
                (key, quantity, price) = line.split()
                drinks[(key)] = quantity, price
        return drinks
        text.close()
    def retVals(self):
        return (self.drink, self.quantity, self.price)
    def setDrink(self, drink):
        self.drink = drink
        self.quantity = self.drinksD[drink][0]
        self.price = self.drinksD[drink][1]
