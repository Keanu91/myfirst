#Initiate
import math
from fractions import Fraction
#variables
order = int() # Hihest Power
acoef = [] # array of Coefficients
apower = [] # array of Powers
answer = [] # array of answer
sumOfAll = [] # sumOfAll when calculating
rangeFrom = float() #lowest x value tested
rangeTo = float() #Highest x value tested
rangeStep = float() #Steps of x values
numerator = int() # numerator
denominator = int() # denominator

print("Range of X values")
rangeFrom = float(input("From "))
rangeTo = float(input("To "))
print("Stepping Every Num/Den")
numerator = int(input("Numerator is "))
denominator = int(input("Denominator is "))
rangeStep = Fraction(numerator,denominator)
print("Number of terms")
order = int(input())


def inputUser(): # taking in input of user
    coef = float()
    power = float()
    print("Enter Coefficient " + str(i))
    coef = input()
    print("Enter Power " + str(i))
    power = input(str(coef)+"x^")
    return(coef,power)

def division(coef,x,power):
    res = float()
    res = float(coef*math.pow(x,power))
    return(res)

def counter(): #calculating each section
    xvalue = Fraction(int(rangeFrom)*1,1) # X value
    while xvalue <= rangeTo : #range of x variables tested
        sumVar = [0]
        for i3 in range(0,order):
            sumVar.append(division(acoef[i3],xvalue,apower[i3]))
        sumOfAll.append(sum(sumVar))
        #print(sumVar)
        if sumOfAll[-1] != 0:
            sumOfAll.pop()
        else:
            answer.append(xvalue)
        xvalue += rangeStep #round to avoid long number
#        print(xvalue)

#def rangeOfx():
#    difOfRange = int(rangeTo - rangeFrom)
#    seriesOfValues = [] # series of x values to try
#    for i4 in range(0,round(difOfRange/rangeStep)):
#        seriesOfValues.append(rangeFrom+i4*rangeStep)
#    return(seriesOfValues)


#for i in range(0,order):
#    var = inputUser()
#    acoef.append(float(var[0]))
#    apower.append(float(var[1]))

acoef = [-1176,-2590,-1741,-241,78]
apower = [4,3,2,1,0]

print(acoef)
print(apower)
#calculation

counter()

print("final sumOfAll")
print(sumOfAll)
print(answer)
