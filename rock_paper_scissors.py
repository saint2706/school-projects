"""
A command-line based Rock, Paper, Scissors game.

This module contains the logic and console interface for a simple Rock, Paper,
Scissors game. The game allows a player to compete against the computer for a
specified number of rounds. The player's and computer's choices are determined,
and a winner is announced for each round.

Classes:
    RockPaperScissorsGame: Encapsulates the core game logic.
    RockPaperScissorsConsole: Handles the console interface for the game.

Functions:
    main: The main function to run the game.

Usage:
    To play the game, run this script from the command line:
    $ python rock_paper_scissors.py
"""
import random
from typing import Literal, Optional

Choice = Literal["Rock", "Paper", "Scissors"]

class RockPaperScissorsGame:
    """
    Encapsulates the core logic of a Rock, Paper, Scissors game.

    This class is responsible for determining the computer's choice and
    evaluating the winner of each round. It does not handle any user
    interaction or game flow.

    Attributes:
        player_choice (Optional[Choice]): The player's choice for the current round.
        computer_choice (Optional[Choice]): The computer's choice for the current round.
    """

    def __init__(self) -> None:
        """
        Initializes the RockPaperScissorsGame.

        This sets the initial state of the game, with no choices made yet.
        """
        self.player_choice: Optional[Choice] = None
        self.computer_choice: Optional[Choice] = None

    def get_computer_choice(self) -> Choice:
        """
        Generates a random choice for the computer.

        This method randomly selects one of "Rock", "Paper", or "Scissors"
        for the computer's turn and updates the `computer_choice` attribute.

        Returns:
            Choice: The computer's choice.
        """
        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        return self.computer_choice

    def determine_winner(self, player_choice: Choice, computer_choice: Choice) -> str:
        """
        Determines the winner of a round based on the player's and computer's choices.

        The rules are as follows:
        - Rock beats Scissors
        - Scissors beats Paper
        - Paper beats Rock

        Args:
            player_choice (Choice): The player's choice.
            computer_choice (Choice): The computer's choice.

        Returns:
            str: A message indicating the result of the round (win, lose, or tie).
        """
        # If both choices are the same, it's a tie.
        if player_choice == computer_choice:
            return "Tie!"

        # Define the winning combinations for the player.
        winning_combinations = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }

        # Check if the player's choice beats the computer's choice.
        if winning_combinations[player_choice] == computer_choice:
            return f"You win! {player_choice} beats {computer_choice}."
        else:
            return f"You lose! {computer_choice} beats {player_choice}."

class RockPaperScissorsConsole:
    """
    Handles the console interface for the Rock, Paper, Scissors game.

    This class is responsible for all user interaction, including getting the
    player's choice, displaying round information, and managing the overall
    game flow.

    Attributes:
        game (RockPaperScissorsGame): An instance of the core game logic class.
    """

    def __init__(self) -> None:
        """Initializes the console game and creates a game instance."""
        self.game = RockPaperScissorsGame()

    def get_player_choice(self) -> Choice:
        """
        Prompts the player for their choice and validates it.

        This method will continuously prompt the user until a valid choice
        ("Rock", "Paper", or "Scissors") is entered. The input is case-insensitive.

        Returns:
            Choice: The player's validated choice.
        """
        while True:
            # Prompt the user for their choice.
            choice = input("Rock, Paper, Scissors? ").capitalize()
            # Validate the user's input.
            if choice in ["Rock", "Paper", "Scissors"]:
                return choice
            else:
                print("That's not a valid play. Please choose Rock, Paper, or Scissors.")

    def play_round(self) -> None:
        """
        Plays a single round of Rock, Paper, Scissors.

        This method gets the player's and computer's choices, displays them,
        determines the winner, and prints the result.
        """
        player_choice = self.get_player_choice()
        computer_choice = self.game.get_computer_choice()

        print(f"You chose {player_choice}, computer chose {computer_choice}.")
        result = self.game.determine_winner(player_choice, computer_choice)
        print(result)

    def play_game(self) -> None:
        """
        Handles the main game loop, including the number of rounds.

        This method prompts the user for the number of rounds to play and
        then iterates through the rounds, calling `play_round` for each one.
        """
        try:
            # Get the number of rounds from the user.
            num_rounds_str = input('Enter the number of rounds to play: ')
            num_rounds = int(num_rounds_str)
        except ValueError:
            # Handle cases where the user enters non-numeric input.
            print("Invalid number of rounds. Please enter a number.")
            return

        # Play the specified number of rounds.
        for i in range(num_rounds):
            print(f"\n--- Round {i + 1} ---")
            self.play_round()

def main() -> None:
    """
    Main function to run the Rock, Paper, Scissors game.

    This function creates a console instance and starts the game loop.
    It also asks the player if they want to play again after each game.
    """
    console = RockPaperScissorsConsole()
    # Main game loop
    while True:
        console.play_game()
        # Ask the player if they want to play again.
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            break
    print("Thanks for playing!")

# This ensures that the main() function is called only when the script is executed directly.
if __name__ == "__main__":
    main()