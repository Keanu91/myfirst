import math


def userInput():
    print("Input Start Value")
    startVal = int(input())
    print("Input p.a. rate as percentage eg(5)")
    rateVal = int(input())
    print("Input 1 for week based or 2 for monthly based or 3 for yearly based")
    selectionVal = int(input())
    for i in range(1,4):
        if selectionVal == i:
            print("Input number of unit time to compund eg(2 for compund every 2 months)")
            deviationVal = int(input())
            break
    rate = float()
    return()



userInput()
