import random


words = ["rabbit" , "madrid" , "camel", "about" , "ability" , "tokyo" , "riyadh" , "school"  , "munich" , "boy"]


choosen = random.choice(words)

endOfGame  = False

playerlives = 6

wordlist = []


for i in choosen:
    wordlist.append("_")




while not endOfGame:
    userinput = input("guess the letter ").lower()
    for i in range(len(choosen)):
        letter = choosen[i]
        if letter == userinput:
            wordlist[i] = letter
    if userinput not in wordlist:
        playerlives -= 1
    if playerlives == 0:
        endOfGame = True
    if playerlives == 3:
        print(f"hint the name starts {choosen[0]} ends with {choosen[-1]}")
            
    print(wordlist)
    if "_" not in wordlist:
        endOfGame = True









