
def userinput():
    in1 = input("Enter the lower number \n")
    in2 = input("Enter the higher number \n")
    return[in1,in2]

def numcheck(in1):
    for i in range(len(in1)):
        if in1[i].isnumeric() is False:
            return False
        else:
            i=i+1
    return True

print("Welcome to Keaun's Number Guessing Game \n")
print("To begin please enter a rg")

rg=userinput()

while numcheck(rg) is False:
    print("An entry was non-numeric please try again")
    rg = userinput()

print(rg)
