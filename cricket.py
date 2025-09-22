import random
import time

class CricketGame:
    """
    Represents a simple game of cricket.
    """
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.target = 0

    def _play_inning(self, batting_first):
        """
        Simulates one inning of the game.

        Args:
            batting_first (str): "player" or "computer"

        Returns:
            int: The score of the inning.
        """
        score = 0
        while True:
            try:
                if batting_first == "player":
                    player_choice = int(input("Enter a number from 1 to 6: "))
                    if not 1 <= player_choice <= 6:
                        print("Invalid input. Please enter a number between 1 and 6.")
                        continue
                else:
                    player_choice = random.randint(1, 6)
                    print(f"Computer chose: {player_choice}")

                computer_choice = random.randint(1, 6)
                print(f"Computer chose: {computer_choice}")

                if player_choice == computer_choice:
                    print("Out!")
                    break
                else:
                    if batting_first == "player":
                        score += player_choice
                    else:
                        score += computer_choice
                    print(f"Current score: {score}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        return score

    def play(self):
        """Main function to play the game."""
        print("Welcome to Cricket!")

        # Toss
        toss_choice = input("Enter 'heads' or 'tails': ").lower()
        coin_toss = random.choice(["heads", "tails"])

        player_won_toss = toss_choice == coin_toss

        if player_won_toss:
            print("You won the toss!")
            choice = input("What do you want to choose? (batting/balling): ").lower()
        else:
            print("You lost the toss.")
            choice = random.choice(["batting", "balling"])
            print(f"The computer chose {choice}.")

        if choice == "batting":
            print("\n--- You are batting ---")
            self.player_score = self._play_inning("player")
            print(f"You scored {self.player_score}. Target for computer is {self.player_score + 1}.")
            self.target = self.player_score + 1

            print("\n--- Computer is batting ---")
            self.computer_score = self._play_inning("computer")
        else: # balling
            print("\n--- Computer is batting ---")
            self.computer_score = self._play_inning("computer")
            print(f"Computer scored {self.computer_score}. Target for you is {self.computer_score + 1}.")
            self.target = self.computer_score + 1

            print("\n--- You are batting ---")
            self.player_score = self._play_inning("player")

        self._show_result()

    def _show_result(self):
        """Displays the result of the game."""
        print("\n--- Game Over ---")
        print(f"Your score: {self.player_score}")
        print(f"Computer's score: {self.computer_score}")

        if self.player_score > self.computer_score:
            print("You won the game!")
        elif self.computer_score > self.player_score:
            print("You lost the game!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    game = CricketGame()
    game.play()
    print("\nThank You for playing!")
