from cryptography.fernet import Fernet


''' 
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


def load_key():
    with open("key.key", "rb") as f:
        key = f.read()
        return key


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user}, Password: {fer.decrypt(passw.encode()).decode()}")


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(f"{name} | {fer.encrypt(pwd.encode()).decode()} \n")


while True:
    mode = input("Would you like to add a new password or view the existing ones(View/Add) or press Q to quit?\n")

    if mode.lower() == "q":
        break

    if mode.lower() == "view":
        view()
    elif mode.lower() == "add":
        add()
    else:
        print("Not a valid option")
        continue
