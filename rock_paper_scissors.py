import random
from typing import Literal, Optional

Choice = Literal["Rock", "Paper", "Scissors"]

class RockPaperScissorsGame:
    """
    Encapsulates the core logic of a Rock, Paper, Scissors game.
    """

    def __init__(self) -> None:
        """Initializes the game."""
        self.player_choice: Optional[Choice] = None
        self.computer_choice: Optional[Choice] = None

    def get_computer_choice(self) -> Choice:
        """
        Generates a random choice for the computer.

        Returns:
            Choice: The computer's choice.
        """
        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        return self.computer_choice

    def determine_winner(self, player_choice: Choice, computer_choice: Choice) -> str:
        """
        Determines the winner of a round based on the choices.

        Args:
            player_choice (Choice): The player's choice.
            computer_choice (Choice): The computer's choice.

        Returns:
            str: A message indicating the result of the round.
        """
        if player_choice == computer_choice:
            return "Tie!"

        winning_combinations = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }

        if winning_combinations[player_choice] == computer_choice:
            return f"You win! {player_choice} beats {computer_choice}."
        else:
            return f"You lose! {computer_choice} beats {player_choice}."

class RockPaperScissorsConsole:
    """
    Handles the console interface for the Rock, Paper, Scissors game.
    """

    def __init__(self) -> None:
        """Initializes the console game."""
        self.game = RockPaperScissorsGame()

    def get_player_choice(self) -> Choice:
        """
        Prompts the player for their choice and validates it.

        Returns:
            Choice: The player's validated choice.
        """
        while True:
            choice = input("Rock, Paper, Scissors? ").capitalize()
            if choice in ["Rock", "Paper", "Scissors"]:
                return choice
            else:
                print("That's not a valid play. Please choose Rock, Paper, or Scissors.")

    def play_round(self) -> None:
        """Plays a single round of Rock, Paper, Scissors."""
        player_choice = self.get_player_choice()
        computer_choice = self.game.get_computer_choice()

        print(f"You chose {player_choice}, computer chose {computer_choice}.")
        result = self.game.determine_winner(player_choice, computer_choice)
        print(result)

    def play_game(self) -> None:
        """Handles the main game loop."""
        try:
            num_rounds = int(input('Enter the number of rounds to play: '))
        except ValueError:
            print("Invalid number of rounds. Please enter a number.")
            return

        for i in range(num_rounds):
            print(f"\n--- Round {i + 1} ---")
            self.play_round()

def main() -> None:
    """Main function to run the game."""
    console = RockPaperScissorsConsole()
    while True:
        console.play_game()
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()