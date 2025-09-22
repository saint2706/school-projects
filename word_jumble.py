import random

class WordJumble:
    """
    Represents a word jumble game.
    """
    def __init__(self):
        self.words_and_hints = {
            "python": "It's a snake...",
            "mouse": "It's a rat",
            "easy": "Opposite of hard",
            "difficult": "Synonym of hard",
            "answer": "It is given for a question",
            "xylophone": "It is a toy...",
            "mirror": "What is deaf, dumb and blind, but always tells the truth?",
            "staircase": "What goes up and down without moving?"
        }
        self.word_to_guess = ""
        self.jumbled_word = ""

    def setup_game(self):
        """Sets up a new game."""
        self.word_to_guess = random.choice(list(self.words_and_hints.keys()))

        temp_word = self.word_to_guess
        self.jumbled_word = ""
        while temp_word:
            position = random.randrange(len(temp_word))
            self.jumbled_word += temp_word[position]
            temp_word = temp_word[:position] + temp_word[(position + 1):]

    def play(self):
        """Main function to play the game."""
        print("Welcome to Word Jumble!")
        print("Unscramble the letters to make a word.")
        print("(Press the enter key at the prompt to quit.)")

        while True:
            self.setup_game()
            print(f"\nThe jumbled word is: {self.jumbled_word}")

            while True:
                guess = input("\nYour guess: ").lower()

                if guess == self.word_to_guess:
                    print("That's it! You guessed it!\n")
                    break
                elif guess == "":
                    print("You quit.")
                    break
                else:
                    print("Sorry, that's not it.")
                    hint_choice = input("Do you need a hint? (y/n): ").lower()
                    if hint_choice == 'y':
                        print(f"Hint: {self.words_and_hints[self.word_to_guess]}")

            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                break

        print("Thanks for playing.")

if __name__ == "__main__":
    game = WordJumble()
    game.play()
