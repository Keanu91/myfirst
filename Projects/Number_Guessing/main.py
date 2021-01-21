import random

def userinput():
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

def inrange(var1,var2):
    if int(var2[0]) <= int(var1[0]) <= int(var2[1]):
        return True
    else:
        return False

def closeguess(guess,actual,maxr):
    i=int(1)
    while i <= maxr:
        UpLo=[]
        UpLo.append(actual-i)
        UpLo.append(actual+i)
        print(UpLo)
        if inrange(guess,UpLo) is True:
            return i
        else:
            i=i*10

print("Welcome to Keaun's Number Guessing Game \n")
print("To begin please enter a range")

rg=userinput() #rg is range

num = random.randint(int(rg[0]), int(rg[1]))

while numcheck(rg) is False: #Call function to check input
    print("An entry was non-numeric please try again")
    rg = userinput()

renge=int(rg[1])-int(rg[0])
guess=[0]

while int(guess[0]) != int(num):

    guess = guessinput()

    while numcheck(guess) is False: #Call function to check input
        print("An entry was non-numeric please try again")
        guess = guessinput()

    while inrange(guess, rg) is False:
        print("That guess was outside the range silly\nTry again")
        guess = guessinput()

    #closeguess(guess,num,renge)

    #print("asjdn")
print("Congrats u GOT IT\nThe number was "+str(guess[0]))
