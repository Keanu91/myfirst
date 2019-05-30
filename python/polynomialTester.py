#Initiate
import math
order = int()
print("Order of polynomial")
order = int(input())
acoef = []
apower = []
answer = []
sumOfAll = []

def inputUser(): # taking in input of user
    coef = int()
    power = int()
    print("Enter Coefficient " + str(i))
    coef = int(input())
    print("Enter Power " + str(i))
    power = int(input(str(coef)+"x^"))
    return(coef,power)

def division(coef,x,power):
    res = float()
    res = float(coef*math.pow(x,power))
    return(res)

def counter(): #calculating each section
    for i2 in range(-100,100): #ramge of x variables tested
        global x
        x = i2
        count = [0]
        for i3 in range(0,order+1):
            count.append(division(acoef[i3],x,apower[i3]))
            print(count)
        sumOfAll.append(sum(count))
        if sumOfAll[-1] != 0:
            sumOfAll.pop()
        else:
            answer.append(x)

for i in range(0,order+1):
    var = inputUser()
    var1 = var[0]
    var2 = var[1]
    acoef.append(var1)
    apower.append(var2)

#calculation

counter()
print("final sumOfAll")
print(sumOfAll)
print(answer)
