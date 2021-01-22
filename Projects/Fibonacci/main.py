
x = input("put in a number\n")
length = len(x)
guess=str("x")
fibb=[0,1]
finished = 0
while finished != 1:
    fibb.append(fibb[0]+fibb[1])
    var = str(fibb[2])
    while len(var) > 0:
        guess = guess + var[0]
        var = var[1:]
        print(guess)
        if str(guess) == str(x):
            finished = 1
        if len(guess) == length:
            guess=guess[1:]
    del fibb[0]
print(fibb)
