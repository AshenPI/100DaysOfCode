print("welcome to the tip calculator")

Total = float(input("what is the total bill ? "))

numOFpeople = int(input("how many people to split the bill "))

percentage = float(input("what percentage to tip would you like to give? 10 ,12, 15 , 20 "))


Total =  Total / numOFpeople

if percentage == 10:
    n1ewTotal = 0.10 * Total
    Total+= n1ewTotal
   
    print(f"each person should pay {Total:.2f}")
elif percentage == 12:
    n2ewTotal = 0.10 * Total
    Total+= n2ewTotal
    print(f"each person should pay {Total:.2f}")
elif percentage == 15:
    n3ewTotal = 0.10 * Total
    Total+= n3ewTotal
    print(f"each person should pay {Total:.2f}")
elif percentage == 20:
    n4ewTotal = 0.10 * Total
    Total+= n4ewTotal
    print(f"each person should pay {Total:.2f}")
else:
    print(f"each person should pay {Total:.2f}")


