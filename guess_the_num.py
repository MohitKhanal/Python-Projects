import random
integer=random.randint(1,10)
gifts=["Cadbury Dairy Milk","WaiWai Noodles","Cheeseballs","Melody","Kurkure"]
print("We are here to play a game.I have selected a number between 1 to 10.You have only 3 chances to guess!")
print("If you guessed it right,you will get these gifts randomly!")
for items in gifts:
    print(items)
for i in range(3,0,-1):
    num_input=int(input("Enter your guess:"))
    if num_input==integer:
        print(f"Congratulations!You have guessed right!!")
        print("You have won",random.choice(gifts))
        break
    else:
        if i==1:
            print(f"You are out of the game.The correct number was {integer}")
            break
        print(f"You have still {i-1} attempts left")
