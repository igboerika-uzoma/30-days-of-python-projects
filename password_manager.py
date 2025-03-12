import os
master_pwd = input("What is the master password: ")


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.read():
            print(line)


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + " " + pwd + "\n")

def remove():
    name = input("Account name to remove: ")
    if not os.path.exists('passwords.txt'):
        print("No passwords saved yet.")
        return

    with open('passwords.txt', 'r') as f:
        lines = f.readlines()

    with open('passwords.txt', 'w') as f:
        for line in lines:
            if not line.startswith(name + " "):
                f.write(line)
            else:
                print(f"Removed password for account: {name}")

while True:
    mode = input("Would you like to add a new password or view a saved one? (add/view) type q to stop ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "remove":
        remove()




