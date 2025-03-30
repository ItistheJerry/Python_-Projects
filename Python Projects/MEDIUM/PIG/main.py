# PIG = Multiplayer Game Die Rolling if won we store our rolling digit but also deletes as much as we roll 

import random

def roll():
    min_Val = 1
    max_val = 6
    roll = random.randint(min_Val, max_val)

    return roll


num_Players = int(input("Enter the number of players (1-4): \n"))
while True:
    if 2 <= num_Players <= 4:
        break
    else:
        print("Must be between 2 - 4 players. Try Again\n")
        break

max_score = 50
# will change list size based on no. of players and will consist of all players scores.
player_scores = [0 for _ in range((num_Players))]

while max(player_scores) < max_score:

    for player_idx in range(num_Players):
        print(f"\nPlayer {player_idx + 1} turn has just started \n")
        print(f"Your Total Score is: {player_scores[player_idx]}\n")
        current_score = 0

    while True:
        should_roll = input("Would you like to roll (y)? or q(quit): \n").lower()
        if should_roll != "y":
            break
    
        value = roll()
        if value == 1:
            print("You Rolled a 1! Turn Done! \n")
            current_score = 0
            break
        else:
            current_score += value
            print(f"You rolled: {value}")

        print(f"Your score is: {current_score}")


    player_scores[player_idx] += current_score
    print(f"Your Current Score is: {player_scores[player_idx]}")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"Player number {winning_idx + 1} is th winner with score of: {max_score}")