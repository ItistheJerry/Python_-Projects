print(f"Welcome To My Computer Quiz!!")

Name = input("Enter Your Name: \n")
playing = input(f"Would You Like to Play My Game {Name}:  (Y/N) \n")

if (playing.lower() != "yes".lower()):
    quit()

print("Okayy! Let's Play :) ")

score = 0

answer = input("What Does CPU stand for?: \n")

if (answer.lower() == "central processing unit".lower()):
    print("Correct Yo!  ")
    score += 1
else:
    print("Yoo Incorrect!! ")


answer = input("What Does GPU stand for?: \n")

if (answer.lower() == "graphics processing unit".lower()):
    print("Correct Yo!  ")
    score += 1
else:
    print("Yoo Incorrect!! ")


answer = input("What Does RAM stand for?: \n")

if (answer.lower() == "random access memory".lower()):
    print("Correct Yo!  ")
    score += 1
else:
    print("Yoo Incorrect!! ")


answer = input("What Does psu stand for?: \n")

if (answer.lower() == "power supply unit".lower()):
    print("Correct Yo!  ")
    score += 1
else:
    print("Yoo Incorrect!! ")


answer = input("What Does ROM stand for?: \n")

if (answer.lower() == "read only memory".lower()):
    print("Correct Yo!  ")
    score += 1
else:
    print("Yoo Incorrect!! ")




print(f"Yo {Name} Earned :{score}: Scores")

percentage = (score/5)*100

print(f"Yo {Name} Earned :{percentage}%:")