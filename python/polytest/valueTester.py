#imports
import math
from fractions import Fraction

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

#print(fractionAtor(aquireVar(0,100)))
