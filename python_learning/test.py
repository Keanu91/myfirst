import math

print("hello World")

string1 = "yo .."
string2 = "wassup"
string3 = string1 + string2

print(string3)

float1 = 563.68453
print("{:5.2f}".format(float1))

float2 = 563.68453
print("%5.2f" % float2)

x = 2
n = 5

power = x ** n
print("%d to the power %d is %d" % (x,n,power))

n=6

power1 = pow(x,n)
print("%s to the power %d is %s" % (x,n,power1))

n=7

power2 = math.pow(x,n)
print("%s to the power %d is %2.2f" % (x,n,power2))
