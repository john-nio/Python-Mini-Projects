import random


# Use a dictionary to store questions and answers. This is a more suitable data structure.
QUESTIONS = {
    "What is CPU?": "Central Processing Unit",
    "What is the Capital of Canada?": "Ottawa",
    "Which is the biggest planet in the Solar system?": "Jupiter",
}


def run_quiz():
    """Runs a single round of the quiz, asks questions, and tracks the score."""
    score = 0
    # Create a list of questions from the dictionary and shuffle them for variety.
    question_items = list(QUESTIONS.items())
    random.shuffle(question_items)

    for question, correct_answer in question_items:
        print(f"\n{question}")
        user_answer = input("Your answer: ")

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    print(f"\nQuiz finished! Your final score is {score}/{len(QUESTIONS)}")


if __name__ == "__main__":
    while True:
        start_game = input("Are you ready to play the game? (y/n): ").lower()
        if start_game == "y":
            run_quiz()
        elif start_game == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
