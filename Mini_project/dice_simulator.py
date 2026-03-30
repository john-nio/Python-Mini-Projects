import random

x = input("Do you want to play dice y/n?")

while x == "y":
    rnd = random.randint(1, 6)
    if rnd == 1:
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")

    elif rnd == 2:
        print("---------")
        print("|   0   |")
        print("|   0   |")
        print("|       |")
        print("|       |")
        print("|       |")
        print("---------")

    elif rnd == 3:
        print("---------")
        print("|   0   |")
        print("|   0   |")
        print("|   0   |")
        print("|       |")
        print("|       |")
        print("---------")

    elif rnd == 4:
        print("---------")
        print("|       |")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("|       |")
        print("---------")

    elif rnd == 5:
        print("---------")
        print("|       |")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("|       |")
        print("---------")

    else:
        print("---------")
        print("|       |")
        print("| 0 0 0 |")
        print("|       |")
        print("| 0 0 0 |")
        print("|       |")
        print("---------")
    x = input("Do you want to play dice y/n?")
