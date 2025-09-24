import random

class NumberGuesser:
    """
    Represents a number guessing game.
    """
    def __init__(self):
        self.points = 0

    def play(self):
        """Main function to play the game."""
        print("--- Number Guesser ---")
        print("You initially have 0 points.")
        print("For every correct answer you are awarded 3 points and for a wrong answer 1 point is deducted.")
        print("You are allowed to play till your points become -6.")

        while self.points > -6:
            numbers = random.sample(range(1, 26), 9)
            print(f"\nGuess a number from the following list: {numbers}")

            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            secret_number = random.choice(numbers)

            if guess == secret_number:
                print("You win!")
                self.points += 3
            else:
                print(f"You lose! The number was: {secret_number}")
                self.points -= 1

            print(f"Your points: {self.points}")

        print("\nGame Over! You have less than -5 points.")

if __name__ == "__main__":
    game = NumberGuesser()
    game.play()
    print("Thanks for playing!")
