import random
user_score = 0
computer_score = 0

while user_score != 5 and computer_score != 5:
    user = int(input("Pick a number 1-10: \n"))
    computer = random.randint(1, 10)
    total = user + computer
    if total % 2 == 0:
        user_score+=1
        print("Good job you got a point.\n It's " + str(user_score) + "-" + str(computer_score))
    else:
        computer_score += 1
        print("You lost try harder next round.\n It's " + str(user_score) + "-" + str(computer_score))
    if computer_score == 5:
        print("You lost, better luck next time.")
    else:
        print("You won good job!")
    if computer_score == 5 or user_score == 5:
        x = input("Do you want to restart the game?(y or n)\n")
        if x == "y":
            computer_score = 0
            user_score = 0
        else:
            break