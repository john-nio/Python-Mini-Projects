import random


def generate_secret():
    return "".join(random.sample("0123456789", 4))


def start_game():
    secret_number = generate_secret()
    print("Welcome to Cows and Bulls")
    while True:
        guess_number = input("Enter a 4 unique number to guess the number: ")

        if (
            len(guess_number) != 4
            or not guess_number.isdigit()
            or len(set(guess_number)) != 4
        ):
            print("Invalid Number. Enter 4 unique digits")
            continue

        bulls = 0
        cows = 0

        for i in range(4):
            if guess_number[i] == secret_number[i]:
                cows += 1
            elif guess_number[i] in secret_number:
                bulls += 1

        if cows == 4:
            print("You have guessed the number correctly")
            break

        print(f"Cows: {cows}, Bulls: {bulls}")


start_game()
