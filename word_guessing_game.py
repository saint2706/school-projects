import random

class WordGuessingGame:
    """
    Represents a word guessing game.
    """
    def __init__(self):
        self.words = ("Mathematics","pizza","pasta","examination","computer", "Python", "Program", "Instructions","mississippi","university",
                      "happy","handsome","heaven","peace","school")
        self.word_to_guess = ""
        self.tries = 5

    def setup_game(self):
        """Sets up a new game."""
        self.word_to_guess = random.choice(self.words)
        self.tries = 5

    def play(self):
        """Main function to play the game."""
        print("Welcome to Word Guess game! Lets test how strong your vocabulary is.\n\t\t Good Luck!")

        while True:
            self.setup_game()
            print(f"\nYou have {self.tries} attempts to guess the word.")
            print(f"\t\tLength of the word: {len(self.word_to_guess)}\n")

            hint = self.word_to_guess[0] + '_ ' * (len(self.word_to_guess) - 2) + self.word_to_guess[-1]
            print(hint)

            while self.tries > 0:
                guess = input("Guess the word: ")

                if guess.lower() == self.word_to_guess.lower():
                    print(f"\nYes! You guessed the word! The word was: {self.word_to_guess}")
                    print(f"You guessed it in {6 - self.tries} tries.")
                    break
                else:
                    self.tries -= 1
                    print("No!")
                    if self.tries > 0:
                        print(f"\nTries remaining: {self.tries}")
                        if self.tries == 3:
                            command = input("Would you like a hint? (y/n): ")
                            if command.lower() == "y":
                                hint = self.word_to_guess[0] + self.word_to_guess[1] + '_ ' * (len(self.word_to_guess) - 4) + self.word_to_guess[-2] + self.word_to_guess[-1]
                                print(f"The second and second last letter of the word is: {hint}")
                    else:
                        print("\nNo! You ran out of tries!")
                        print(f"The word was: {self.word_to_guess}")

            play_again = input("\nPlay again? (y/n): ").lower()
            if play_again != 'y':
                break

        print("Thanks for playing!")

if __name__ == "__main__":
    game = WordGuessingGame()
    game.play()
