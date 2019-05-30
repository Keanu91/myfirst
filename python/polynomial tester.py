#Initiate
import math
order = int()
print("Order of polynomial")
order = int(input())
acoef = []
apower = []
answer = float(0)

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
    print(res)





for i in range(0,order+1):
    var = sec()
    var1 = var[0]
    var2 = var[1]
    acoef.append(var1)
    apower.append(var2)

#if order != len(acoef):
#    print("exit fail")
#    exit()

print("YAY")
#calculation

if order == 2:
    for i2 in range(-10,10):
        for i3 in range(0,order):
            
        x = i2
        answer = answer + division(acoef[0],x,apower[0])
        print(answer)
        answer = answer + division(acoef[1],x,apower[1])
        print(answer)
        answer = answer + division(acoef[2],x,apower[2])
        print(answer)
        if answer == 0:
            break
        answer = float(0)
    print(answer)
