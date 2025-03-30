from cryptography.fernet import Fernet

# function to create a key
'''
def write_key():
   key = Fernet.generate_key()
   with open("key.key", "wb") as key_file:
      key_file.write(key)'''

# function to store the key

def load_key():
   file = open("key.key", "rb")
   key = file.read()
   file.close()
   return key


master_pwd = input("What is the master Password: \n")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

# function to create key
# it will open a file and create a file key.key 





def view():
    with open("/Users/thejoker/Desktop/Python Projects/MEDIUM/Passwordmanager/passwords.txt", 'r') as f:
        for line in f.readlines():
           data = line.strip()
           if "|" not in data:
                print(f"Skipping invalid entry: {data}")
                continue
           user, passw = data.split("|", 1)
           print("User:", user,"\n","Password:", fer.decrypt(passw.encode()).decode(), "\n")




def add():
    name = input("Account name: \n")
    pwd = input("Password: \n")


    with open("/Users/thejoker/Desktop/Python Projects/MEDIUM/Passwordmanager/passwords.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:

    mode = input("Would you like to add an new password or view existing ones (views, add), press q to quit? \n").lower()
    if mode == "q":
     quit()


    if mode == "view":
     view()
    elif mode == "add":
     add()
    else:
     print("Invalid mode.")
     continue