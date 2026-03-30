import random

while True:
    y = random.randint(1, 100)
    x = int(input("Guess the number? "))

    while x != y:
        if abs(x - y) < 5:
            print("You are almost near")
        elif abs(x - y) in range(5, 10):
            print("You are getting there")
        else:
            print("You are far away")

        x = int(input("Guess the number? "))

    print("You guessed the number")

    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        print("Thanks for playing!")
        break
