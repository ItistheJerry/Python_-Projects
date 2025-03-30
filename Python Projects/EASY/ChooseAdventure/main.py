name = input("Enter Your Name I can't call you user everytime it's Disrespectful!: \n")
print(f"Welcome {name} to the game!!")\


answer = input("You are on a dirt Road, It has come to an end but you have two option Right or Left, Type Where?? Or Would You Quit\n ").lower()

if answer == "left":
    answer = input("You have come to a river bank, you can either walk or swim around the bank: \n").lower()
    
    if answer == "swim":
        print("You Swim Accros and were eaten by an alligator!..🙀")
    
    elif answer == "walk":
        print("You Came accross a Dangerous Jungle!..ᅨ, Wait For Next Season!!")
    
    else:
        print("Not Valid, You Loose")
        quit()

elif answer == "right":
    answer = input("Now You've Come accross an ancient Temple, Which Contains Knowledge of ancient Civilizations and Their Secret to POwer, But To Climb As it is above the Clouds, You either Use Ropes Or Go to build a grappling Machine!!: \n").lower()

    if answer == "ropes":
        print("You Started Climbing Through Ropes but it was weak from the Joint so after 100-150ft you fall and the Game is Over!!")

    elif answer == "grappling machine":
        answer = input("As The Machine Is strong and reliable You Reach the Gates of The City Doors, Press Next For next Chapter!!!!: \n").lower()
        
        if answer == "next":
            print("The Game is Further In Developement Please Wait For Next Season!!!")
            
        else:
            quit()

elif answer == "quit" or answer == "q":
    quit()

else:
    print("Not a Valid Option. You loose")

print("Buy Prior For Better Fun!!!! $")