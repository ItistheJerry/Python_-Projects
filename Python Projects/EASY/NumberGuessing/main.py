import random 

print(f"Welcome To My Number Guessing Game!!")


name = input("Hello User Enter your Name: \n")

play = int(input(f"Would you Like To Play The Game MR.{name}: Answer in 1/0 \n"))

if (play != 1):
    print("Ohhh You're Boring dude")
    quit()

print("Okey Dokey Let's Play")

n2g = random.randint(1,100)

attempts = 0

while True:
    try:
        num = int(input("Type a Number Between (1-100): \n"))
        attempts += 1


        if num < n2g:
            print("Too Low! Try")

        elif num > n2g:
            print("Too Hight! Try")

        else:
            print(f"Congrats! You've guessed the correct Number in {attempts} attempts!!:")
            break
    except ValueError:
        print("Please Enter a Valid Number:")

