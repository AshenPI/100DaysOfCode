import random
print("welcome to the Rock Scissors paper game")
while True:
    
    player = int(input("Choose 1-Rock , 2-Scissors , 3-Paper  , tap any other number to exit "))
    Computer = random.randint(1,3)

    if player == 1 and Computer == 1:
        print("you choose Rock ")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
        print("computer choose rock ")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("its a Tie")  
    elif player == 1 and Computer == 2:
        print("you choose rock")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
        print("computer choose scissors")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("you won!!")
    elif player ==1 and Computer == 3:
        print("you choose rock")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
        print("computer choose paper")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("computer won !!")
    elif player ==2 and Computer == 1:
    
        print("you choose Scissors ")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("computer choose rock")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("computer won!!")
    elif player == 2 and Computer == 2:
        print("you choose scissors")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("computer choose scissors")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("its a Tie")
    elif player == 2 and Computer == 3:
        print("you choose scissors")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("computer choose paper")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("you won!")
    elif player == 3 and Computer == 1:
        print("you choose paper")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("computer choose rock")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("you won !!")
    elif player == 3 and Computer == 2:
        print("you choose paper")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("computer choose scissors")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("computer won !!")
    elif player == 3 and Computer == 3:
        print("you choose paper")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("computer choose paper")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("its a Tie")
    else:
        break
    
      
#happy Eid (: 






