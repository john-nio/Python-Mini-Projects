import random

x = input("Do you want to play the game y/n ")

while x != "n":
    if x == "y":
        print(
            random.randint(
                1,
                6,
            )
        )
    else:
        print("Invalid choice")
    x = input("Do you want to play the game y/n ")

print("Thanks for playing the game")
