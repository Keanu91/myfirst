guess = input("put in a number\n")
length = len(guess)
counter = 2
fibseg=str("01") #fib segment for comparing
fibb=[0,1] #fib calculation variable
while str(fibseg) != str(guess):
    fibb.append(fibb[0]+fibb[1])
    counter = counter + 1
    var = str(fibb[2])
    while len(var) > 0 and str(fibseg) != str(guess):
        if len(fibseg) == length:
            fibseg=fibseg[1:]
        fibseg = fibseg + var[0]
        var = var[1:]
        print(fibseg)
    del fibb[0]

print(fibb)
print("Displayed is the %s and %s fibonacci number" % ((counter-1),counter))
