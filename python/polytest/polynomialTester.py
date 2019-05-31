#Initiate
import math
from fractions import Fraction
import valueTester
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

#PRIMER BEGINNING
def aquireVar(start,stop):
    primeNum = []
    for num in range(start,stop + 1):   # prime numbers are greater than 1
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
                else:
                    primeNum.append(num)
                if len(primeNum) > 1:
                    if primeNum[-1] != primeNum[-2]:
                        break
                    else:
                        primeNum.pop()
    return(primeNum)

def fractionAtor(primes):
    print(primes)
    listOfVar = []
    for i in range(0,len(primes)):
        print(i)
        listOfVar.append(Fraction(1,primes[i]))
    return(listOfVar)

def oneOnPrime(start,stop):
    return(fractionAtor(aquireVar(start,stop)))

#PrimerEND

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
        print(oneOnPrime(0,50))
        #xvalue += rangeStep #round to avoid long number
#        print(xvalue)


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
#print(sumOfAll)
print(answer)
