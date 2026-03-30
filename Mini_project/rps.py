import random

choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}


def compare_inputs(user_choice, auto_choice):
    if user_choice == auto_choice:
        print("Match is drawn.")
    elif user_choice == "Rock" and auto_choice == "Scissors":
        print("User Won")
    elif user_choice == "Paper" and auto_choice == "Rock":
        print("User Won")
    elif user_choice == "Scissors" and auto_choice == "Paper":
        print("User Won")
    else:
        print("Computer Won")


def play_game():
    while True:
        while True:
            user_input = input("Enter your input r/p/s: ").lower()
            if user_input in choices:
                break
            print("Invalid Input. Try again.")

        user_choice = choices[user_input]
        auto_choice = random.choice(list(choices.values()))

        print(f"You chose {user_choice}")
        print(f"Computer chose {auto_choice}")

        compare_inputs(user_choice, auto_choice)

        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
