
def wordcheck(var):
#    print("wordcheck")
    if var.isalpha() == True:
        return True
    return False

def onechar(var):
#    print("onechar")
    if len(var) == 1:
        return True
    return False

def guessletter(guess,spot,word):
    if word.find(guess,spot) == -1:
        return False
    result=[]
    while word.find(guess,spot) != -1:
        spot=word.find(guess,spot)+1
        result.append(spot-1)
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
guesses = "*"
display=[]

for i in range(len(word)):
    display.append("")
print(display)

while finished == 0:
    guess=input("Make your " + str(guessnum) + " letter guess\n")

    while wordcheck(guess)!=True or onechar(guess)!=True or guessletter(guess,0,guesses)!=False:
        add = " again?" * i
        print("Looks like you didnt follow the rules"+str(add))
        i=i+1
        guess=input("Make your " + str(guessnum) + " letter guess\n")
        guessnum=guessnum+1

    guesses=guesses+guess

    result=guessletter(guess,0,word)

    if result is False:
        print("Unclucky thats a wrong guess\nTry again")
    else:
        print("Nice guess")
        for i in range(len(result)):
            display[result[i]]=guess
        print("heres the results")
        print(display)

    guessnum=guessnum+1
    var=str("")
    for i in range(len(display)):
        var=var+str(display[i])
    if var == word:
        finished = 1
print("congratulations\n the word was\n"+str(word))
