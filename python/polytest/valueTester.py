#imports
import math
from fractions import Fraction

def aquireVar(start,stop):
    listOfVar = []
    diff = int(stop-start)
    primeNum = []
    for num in range(lower,upper + 1):   # prime numbers are greater than 1
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
                else:
                    primeNum.append(num)
    print(primeNum)




aquireVar(-10,10)
