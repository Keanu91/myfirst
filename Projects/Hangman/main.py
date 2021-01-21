
def wordcheck(var):
    if var.isalpha() == True:
        return True
    return False

def onechar(var):
    if len(var) == 1:
        return True
    return False

def guessletter(guess,spot,word):
    if word.find(guess,spot) == -1:
        return False
    result=[]
    while word.find(guess,spot) != -1:
        spot=word.find(guess,spot)+1
        result.append(spot)
    return(result)



print("Welcome to Keaun's Hangman Game")
print("Please type in the word to be guessed")
word = input()
i=0
while wordcheck(word) != True:
    add = " again?" * i
    print("Looks like you put in a non letter"+str(add))
    word = input("Please type in the word to be guessed\n")
    i=i+1

word.lower()

clear = "\n" * 1000
#print(clear)

print("All righty it is a "+str(len(word))+" letter word")

finished = 0
guessnum = 1

while finished = 0:
    guess=input("Make your "+str(guessnum)" letter guess\n")

    while wordcheck(guess) and onechar(guess) != True:
        add = " again?" * i
        print("Looks like you didnt follow the rules"+str(add))
        i=i+1

    if guessletter(guess,0,word) is False:
        print("Unclucky thats a wrong guess\nTry again")
        guessnum=guessnum+1
    else:
        print("Nice guess")
        
