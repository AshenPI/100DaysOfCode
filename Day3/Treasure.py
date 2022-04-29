print("Welcome to Treasure Island Your mission is to find the treasure")

print(r"""\
        |
              /"\
      T~~     |'| T~~
  T~~ |    T~ WWWW|
  |  /"\   |  |  |/\T~~
 /"\ WWW  /"\ |' |WW|
WWWWW/\| /   \|'/\|/"\
|   /__\/]WWW[\/__\WWWW
|"  WWWW'|I_I|'WWWW'  |
|   |' |/  -  \|' |'  |
|'  |  |LI=H=LI|' |   |
|   |' | |[_]| |  |'  |
|   |  |_|###|_|  |   |
'---'--'-/___\-'--'---'
    
    
    """)

Choice = input("You have arrived choose which path Left or Right ? ")
if Choice == "Right":
    print("you fell in trap.. GameOver")
else:
    Choice1 = input("Swim or wait ")
    if Choice1 == "Swim":
        print("you drowned GameOver")
    else:
        choice2 = input("which door Red , Blue , Yellow ")
        if choice2 == "Red":
            print("GameOver")
        elif choice2 == "Blue":
            print("GameOver")
        else:
            print("you won the treasure !!!!!")
            