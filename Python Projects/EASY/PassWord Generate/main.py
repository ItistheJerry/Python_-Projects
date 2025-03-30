import random 
import string # for grabbing lower and upper case and digits and symbols that exist 

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation


    character = letters # as we will always have letters
    if numbers:
        character += digits # if true as numbers we take digits inside string and will add to letter string
    if special_characters:
        character += special # if special we add those too which we will select

    # loop:
    pwd = "" # password
    meet_criteria = False # will set to true once the password sets to the criteria which includes number special characters with letters atlest either numb or special
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length: # while the criteria setted is not met or the length of the generated password isn't upto the length we will let it add more characters
        new_char = random.choice(character)
        pwd += new_char


        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special

    return pwd


min_length = int(input("Enter the minimum length: \n"))
has_number = input("Do you want to have a numbers (y/n): \n").lower() == "y"
has_special = input("Do you want to add special character (y/n): \n").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print(f"The Generated Password is: \n{pwd}\n")