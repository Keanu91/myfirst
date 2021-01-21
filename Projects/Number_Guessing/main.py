
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
    guess = input("Please enter your guess\n")
    return[guess]

print("Welcome to Keaun's Number Guessing Game \n")
print("To begin please enter a range")

rg=userinput() #rg is range

while numcheck(rg) is False: #Call function to check input
    print("An entry was non-numeric please try again")
    rg = userinput()

g1 = guessinput()

while numcheck(g1) is False: #Call function to check input
    print("An entry was non-numeric please try again")
    g1 = guessinput()
