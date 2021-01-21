import random

def userinput(): #taking initial range of random number to be generated
    in1 = input("Enter the lower number \n")
    in2 = input("Enter the higher number \n")
    return[in1,in2]

def numcheck(in1): #Determines if input is numerical
    for i in range(len(in1)):
        if in1[i].isnumeric() is False:
            return False
        else:
            i=i+1
    return True

def guessinput(): #function for user guesses
    g = input("Please enter your guess\n")
    return[g]

def inrange(var1,var2): #function to determine if input is within a given range
    if int(var2[0]) <= int(var1[0]) <= int(var2[1]):
        return True
    else:
        return False

def closeguess(guess,actual): #using intervals of n determines how close guess is
    i=int(1)
    n=5
    while i <= maxr:
        UpLo=[]
        UpLo.append(actual-i)
        UpLo.append(actual+i)
        if inrange(guess,UpLo) is True:
            if int(guess[0]) == int(actual):
                return()
            else:
                return("Your are within "+str(i))
        else:
            i=i+n
    return()

print("Welcome to Keaun's Number Guessing Game \n")
print("To begin please enter a range")

rg=userinput() #rg is range

num = random.randint(int(rg[0]), int(rg[1])) #generate random number

while numcheck(rg) is False: #Call function to check input
    print("An entry was non-numeric please try again")
    rg = userinput()

maxr=int(rg[1])-int(rg[0])
guess=[0]

while int(guess[0]) != int(num): #loop until guess is correct

    guess = guessinput()

    while numcheck(guess) is False: #Call function to check input
        print("An entry was non-numeric please try again")
        guess = guessinput()

    while inrange(guess, rg) is False: #Check if guess is within range
        print("That guess was outside the range silly\nTry again")
        guess = guessinput()

    print(closeguess(guess,num))

print("Congrats u GOT IT\nThe number was "+str(guess[0]))
