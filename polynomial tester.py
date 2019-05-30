#Initiate
import math
order = int()
print("Order of polynomial")
order = int(input())
acoef = []
apower = []

def sec():
    coef = int()
    power = int()
    print("Enter Coefficient " + str(i))
    coef = int(input())
    print("Enter Power " + str(i))
    power = int(input())
    return(coef,power)

def division(x,coef,power):
    res = float()
    res = float(coef*math.pow(x,power))
    print(res)





for i in range(0,order):
    var = sec()
    var1 = var[0]
    var2 = var[1]
    acoef.append(var1)
    apower.append(var2)

if order != len(acoef):
    print("exit fail")
    exit()

print("YAY")
#calculation

 if order == 2:
     for i2 in range(-10,10):
