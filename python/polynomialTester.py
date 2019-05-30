#Initiate
import math
order = int()
print("Order of polynomial")
order = int(input())
acoef = []
apower = []
answer = []
sumOfAll = []


acoef = [1,-4,-12]
apower = [2,1,0]

def sec():
    coef = int()
    power = int()
    print("Enter Coefficient " + str(i))
    coef = int(input())
    print("Enter Power " + str(i))
    power = int(input())
    return(coef,power)

def division(coef,x,power):
    res = float()
    res = float(coef*math.pow(x,power))
    return(res)

def counter():
    for i2 in range(-10,10):
        global x
        x = i2
        count = [0]
        count.append(division(acoef[0],x,apower[0]))
        print(count)
        count.append(division(acoef[1],x,apower[1]))
        print(count)
        count.append(division(acoef[2],x,apower[2]))
        print(count)
        sumOfAll.append(sum(count))
        if sumOfAll[-1] != 0:
            sumOfAll.pop()
        else:
            answer.append(x)
    return("Success")

#for i in range(0,order+1):
#    var = sec()
#    var1 = var[0]
#    var2 = var[1]
#    acoef.append(var1)
#    apower.append(var2)


print("YAY")
#calculation

if order == 2:
    counter()
    print("final sumOfAll")
    print(sumOfAll)
    print(answer)
