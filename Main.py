from datetime import datetime
from Drinks import Drinks
from Glass import Glasses
from Extras import Extras

queue=int(input("Enter how many customers are in the queue: "))

x=0

MyDrink = Drinks()
MyGlass = Glasses()
MyExtra = Extras()

while x < queue:
    dName = str(input("Enter a drink name: "))
    while dName not in MyDrink.drinksD.keys():
        dName = str(input("Enter a CORRECT drink name: "))
    MyDrink.setDrink(dName)
    drink, quantity, price = MyDrink.retVals()
    drinkAmmountQuestion = int(input("How many glasses of "+ drink + " does the customer want? " ))

    gName = str(input("Enter a glass name: "))
    gColor = str(input("Enter a glass color: "))
    while (gName, gColor) not in MyGlass.glassesD.keys():
        if gName not in MyGlass.glassesD:
            gName = str(input("Enter a correct glass name: "))
        else:
            pass
        if gColor not in MyGlass.glassesD:
            gColor = str(input("Enter a correct color name: "))
        else:
            pass
    
    MyGlass.setGlass(gName,gColor)
    glass, color, ammount = MyGlass.retG()


    extraQuestion = str(input("Does the customer want an extra side with his drink: "))
    extraCost = 0

    if extraQuestion == "yes":
        extraNumber = int(input("How many bags does the customer want: "))
        eName = str(input("Enter an extras name: "))
        eFlavour = str(input("Enter an extras flavour: "))
        while (eName, eFlavour) not in MyExtra.extrasD.keys():
            eName = str(input("Enter a correct extra name: "))
            eFlavour = str(input("Enter a correct flavour name: "))
        MyExtra.setExtra(eName,eFlavour)
        extra, flavour, quantityE, priceE = MyExtra.retExtr()
        extraCost = float(priceE)*extraNumber
    elif extraQuestion == "no":
        pass

    finalPrice = extraCost + (float(price)*drinkAmmountQuestion)

    print("\nThe customer has ordered: \n" + str(
        drinkAmmountQuestion) + " glasses of " + drink + "\n" + "Which cost: \n" + price + " /glass \n" + "In  " + color + " " + glass + " glass\n")

    if extraQuestion == "yes":
        print("The customer also wanted \n" + str(
            extraNumber) + " bags of " + flavour + " " + extra + " which cost " + priceE + " /bag")
    print("\nThe total cost is: " + "{0:.2f}".format(finalPrice) + "£")

    with open ("orders.txt", "a") as orders:
        print("\nThe customer has ordered: \n"+ str(drinkAmmountQuestion) + " glasses of " + drink + "\n" + "Which cost: \n"+ price + " /glass \n" + "In  " + color + " " + glass + " glass\n", file=orders)

        if extraQuestion == "yes":
            print("The customer also wanted \n" + str(extraNumber) + " bags of " + flavour + " " + extra + " which cost " + priceE + " /bag", file=orders)
        print("\nThe total cost is: "+ "{0:.2f}".format(finalPrice) + "£\n", file=orders)
        print("The date and time when this order was completed: "+ str(datetime.now())+"\n", file=orders)
    orders.close()

    x+=1