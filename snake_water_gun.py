import random
print("Welcome in Snake Water Gun ")
lst=['snake','water','gun']
i=0
print(f" You have 5 Attempts left")

while i<5 and i>=0:
    i=i+1
    player_choice=input("Choose\n S--> Snake , W-->Water ,G--> Gun ").lower()

    if player_choice!="w" and player_choice!="g" and player_choice!="s":
        print("Invalid Input !\n Please run the command again")   
        exit()

    if player_choice=="s":
        choice=random.choice(lst)
        if choice=="snake":
            print(f"Tie , Computers input was {choice}.")
            print(f" No. of Attempts left : {5-i}")
        if choice=="water":
            print(f"Congrats, You Win..\n Computers input was {choice}.")
            print(f" No. of Attempts left : {5-i}")
        if choice=="gun":
            print(f"Ohho, You lost..\n Computers input was {choice},")
            print(f" No. of Attempts left : {5-i}")

    if player_choice=="w":
        choice=random.choice(lst)
        if choice=="water":
            print(f"Tie , Computers input was {choice}.")
            print(f" No. of Attempts left : {5-i}")
        if choice=="snake":
            print(f"Congrats, You Win..\n Computers input was {choice}.")
            print(f" No. of Attempts left : {5-i}")
        if choice=="gun":
            print(f"Ohho, You lost..\n Computers input was {choice}.")
            print(f" No. of Attempts left : {5-i}")

    if player_choice=="g":
        choice=random.choice(lst)
        if choice=="gun":
            print(f"Tie , Computers input was {choice}.")
            print(f" No. of Attempts left : {5-i}")
        if choice=="snake":
            print(f"Congrats, You Win..\n Computers input was {choice}.")
            print(f" No. of Attempts left : {5-i}")
        if choice=="water":
            print(f"Ohho, You lost..\n Computers input was {choice}.")
            print(f" No. of Attempts left : {5-i}")

print("Thankyou for playing..! GoodBye, have a nice day")

print(" \t\t\t\t\t\t\t\t Made by Deepanshu Singhal..!")