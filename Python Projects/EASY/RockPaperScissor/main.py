import random

print("Welcome Players!!")

user_wins = 0
computer_wins = 0

# def score():
#     print(f"Score huh! You have {user_wins} scores and Me have scored {computer_wins}, anyway lets playe again shall we!!!")

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Scissor/Paper or Q to Quit: \n").lower()
    if user_input == "q":
        break

    # if user_input == score:
    #     print(score)


    if user_input not in options:
        continue # for Reasking them


    random_num = random.randint(0, 2)
    # rock: 0, paper: 1, scissor: 2
    computer_pick = options[random_num]

    print(f"Computer Picked {computer_pick}.")


    if user_input == "rock" and computer_pick == "scissor":
        print("Well You Won this Round")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "rock":
        print("I won This Round:")
        computer_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won this round user!!")
        user_wins += 1
    elif user_input == "rock" and computer_pick == "paper":
        print("As it should be i won")
        computer_wins += 1
    elif user_input == "paper" and computer_pick == "scissor":
        print("I won user")
        computer_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("Mistakes happen u won")
        user_wins += 1
    elif user_input == computer_pick:
        print("See how that turned out you looked didn't you!!")
    else:
        print("Not Correct Input!!")



print(f"User won {user_wins} times")
print(f"I won {computer_wins} times")
print("GoodbyE!!")