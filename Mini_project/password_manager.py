def add():
    user_name = input("Enter your Username: ")
    pwd = input("Enter your Password: ")
    with open("passwords.txt", "a") as f:
        f.write(user_name + "|" + pwd + "\n")


def view():
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                data = line.rstrip()

                user, password = data.split("|", 1)
                print(f"Username is: {user}")
                print(f"Password is: {password}")
    except FileNotFoundError:
        print("No passwords saved yet. Add a password first.")


while True:
    x = input("Would you like to view or add password or quit: ")
    if x.lower() == "v":
        view()
    elif x.lower() == "a":
        add()
    elif x.lower() == "q":
        print("See you again!")
        break
    else:
        print("Invalid Choice Use either v or a or q")
