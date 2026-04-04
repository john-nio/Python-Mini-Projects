import random


def player_choice():
    while True:
        try:
            player_number = int(
                input("How many players do you want to include (2 to 4)? ")
            )
            if player_number == 1:
                print("There should be more than 1 player to continue.")
            elif 1 < player_number < 5:
                print("Let's start the game!")
                return player_number
            else:
                print("Invalid Choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def dice_roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)


def play_game():
    num_players = player_choice()
    scores = [0 for _ in range(num_players)]
    target_score = 20  # The first player to reach this score wins

    while max(scores) < target_score:
        for player_idx in range(num_players):
            print(f"\n--- Player {player_idx + 1}'s Turn ---")
            print(f"Your total score is: {scores[player_idx]}")
            current_turn_score = 0

            while True:
                choice = input("Press 'r' to roll or 'h' to hold: ").lower()
                if choice == "h":
                    break
                elif choice == "r":
                    roll = dice_roll()
                    if roll == 1:
                        print(
                            "You rolled a 1! Your turn is over. You lost all points for this turn."
                        )
                        current_turn_score = 0
                        break
                    else:
                        current_turn_score += roll
                        print(
                            f"You rolled a {roll}! Current turn score: {current_turn_score}"
                        )
                else:
                    print("Invalid choice. Please press 'r' or 'h'.")

            scores[player_idx] += current_turn_score
            print(f"Player {player_idx + 1}'s total score is now {scores[player_idx]}")

            if scores[player_idx] >= target_score:
                print(
                    f"\n🎉 Congratulations! Player {player_idx + 1} wins with a score of {scores[player_idx]}! 🎉"
                )
                return  # End game


if __name__ == "__main__":
    play_game()
