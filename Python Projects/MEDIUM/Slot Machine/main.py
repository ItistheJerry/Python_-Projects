import random

MAX_LINES = 4
MAX_BET = 100
MIN_BET = 10

# number and rows on the slot machine 
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def deposit():
    while True:
        try:
            amount = int(input("\n How much would you deposit: \n$"))
            if amount > 0:
                return amount
            else:
                print("\n Amount must be greater than 0.\n")

        except ValueError:
            print("\n Enter a Number Would ya?:\n")

        

# amount = deposit()
# print(f"\n Deposited amount: {amount}")

# collecting bet from users, determine how much they wanna bet, and how many lines on the bet and then multiply the number of lines with the betting amount
def get_lines():
    while True:
        try:
            lines = int(input("\n How much Lines (1-" + str(MAX_LINES) + ")?\n"))
            if 1 <= lines <=  MAX_LINES:
                return lines
            else:
                print("\n Amount of lines should be within the options.\n")

        except ValueError:
            print("\n Enter a Number Would ya?:\n")

def get_bet():
    while True:
        try:
            amount = int(input("\n How much would you bet on each line: \n$"))
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"\n Amount must be between ${MIN_BET} - ${MAX_BET}\n")

        except ValueError:
            print("\n Enter a Number Would ya?:\n")


def main():
    balance = deposit()
    lines = get_lines()
    while True:
    
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"\n Not have enough to bet, Your Current balance is ${balance}")
        else:
            break
    print(f"\n You are betting ${bet} on {lines} lines, Hence Total Bet is equal to: ${total_bet}")


main()