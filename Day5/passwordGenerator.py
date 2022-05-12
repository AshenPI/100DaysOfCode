import random 
import string
letters = string.ascii_letters
digits = string.digits
characters = list("!@#$%^&*()")

password = []

def generatePass():

    lettersCount = int(input("How may letters would you like? \n "))
    digitsCount = int(input("How many numbers would you like? \n "))
    charactersCount = int(input("How many symbols would you like? \n "))
    
    
    for i in range(lettersCount):
        password.append(random.choice(letters))
    
    for i in range(digitsCount):
        password.append(random.choice(digits))
    
    for i in range(charactersCount):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    print("".join(password))

generatePass()
