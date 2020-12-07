import random

# ROCK, PAPER, SCISSOR GAME

# Computer Will Choose Rock, Paper And Scissor From Here
sign=["rock","paper","scissor"]
play="y"
print("Welcome to Rock, Paper and Scissor Game")
print("---------------------------------------")
print("Rules: \n 1. Only enter Rock, Paper or Scissor. \n 2. Can enter capital and small letter. \n 3. If you enter wrong input computer will get the point.")
print("---------------------------------------")

# To Play Game Again
while play.lower()=="y":
    your_points=0
    comp_points=0
    # Checking If Input Is Integer Or Not 
    try:
        nor=int(input("Enter no of rounds:"))
    except:
        print("Invalid Input: Only enter numbers")
        print("---------------------------------------")
        continue
    print("---------------------------------------")
    # Number Of Rounds
    for x in range(nor):
        # Taking Input From User
        your_sign=input("Enter(rock,paper or scissor):")
        your_sign=your_sign.lower()
        # For Checking If User Entered Valid Input Or Not(Rock, Paper, Scissor)
        if your_sign not in sign:
            print("Invalid input : Enter only rock, paper or scissor | Now computer will get 1 point")
            comp_points+=1
            continue
        # Computer Choosing Random Option From 'sign'
        comp_sign = random.choice(sign)
        print("Your Sign:{}     |     Comp Sign:{}".format(your_sign,comp_sign))
        # Comparing Between Computer Sign And Player Sign And Giving Points According To It
        if your_sign == comp_sign:
            continue
        elif your_sign == "rock" and comp_sign == "paper":
            comp_points+=1
        elif your_sign == "paper" and comp_sign == "rock":
            your_points+=1
        elif your_sign == "paper" and comp_sign == "scissor":
            comp_points+=1
        elif your_sign == "scissor" and comp_sign == "paper":
            your_points+=1
        elif your_sign == "scissor" and comp_sign =="rock":
            comp_points+=1
        elif your_sign == "rock" and comp_sign == "scissor":
            your_points+=1
    # Displaying Points
    print("---------------------------------------")
    print("Your Points:{}   |   Comp Points:{}".format(your_points,comp_points))
    print("---------------------------------------")
    # Displaying Who Won Accrding To Points
    if your_points>comp_points:
        print("You Won By {} points".format(your_points))
    elif your_points<comp_points:
        print("Computer Won By {} points".format(comp_points))
    elif your_points==comp_points:
        print("It's  a tie by {}".format(your_points))
    # For Plaing Again
    print("---------------------------------------")
    play=input("If you want to play again enter 'y':")
    print("---------------------------------------")
print("Thanks For Playing")
print("---------------------------------------")