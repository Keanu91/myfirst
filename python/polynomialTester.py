#Initiate
import math
#variables
order = int() # Hihest Power
acoef = [] # array of Coefficients
apower = [] # array of Powers
answer = [] # array of answer
sumOfAll = [] # sumOfAll when calculating
rangeFrom = float() #lowest x value tested
rangeTo = float() #Highest x value tested
rangeStep = float() #Steps of x values

print("Range of X values")
rangeFrom = float(input("From "))
rangeTo = float(input("To "))
print("Stepping Every")
rangeStep = float(input())
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
    xvalue = rangeFrom # X value
    while xvalue < rangeTo : #range of x variables tested
        sumVar = [0]
        for i3 in range(0,order):
            sumVar.append(division(acoef[i3],xvalue,apower[i3]))
        sumOfAll.append(sum(sumVar))
        if sumOfAll[-1] != 0:
            sumOfAll.pop()
        else:
            answer.append(xvalue)
        xvalue += rangeStep

for i in range(0,order):
    var = inputUser()
    acoef.append(var[0])
    apower.append(var[1])

#calculation

counter()
print("final sumOfAll")
print(sumOfAll)
print(answer)
