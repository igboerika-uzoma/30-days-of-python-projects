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


while True:
    mode = input("Would you like to add a new password or view a saved one? (add/view) type q to stop ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
