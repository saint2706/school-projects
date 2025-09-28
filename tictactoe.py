import os
import random
import time
from typing import List, Literal, Optional

Player = Literal["X", "O"]
GameState = Literal["RUNNING", "WIN", "DRAW"]

class TicTacToe:
    """
    Represents a game of Tic-Tac-Toe, encapsulating the game logic.
    """

    def __init__(self) -> None:
        """Initializes the game board and state."""
        self.board: List[Optional[Player]] = [None] * 9
        self.current_player: Player = "X"
        self.game_state: GameState = "RUNNING"

    def make_move(self, position: int) -> bool:
        """
        Makes a move on the board if the position is valid and available.

        Args:
            position (int): The position to mark (0-8).

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        if not (0 <= position < 9 and self.board[position] is None):
            return False

        self.board[position] = self.current_player
        self.update_game_state()
        if self.game_state == "RUNNING":
            self.switch_player()
        return True

    def switch_player(self) -> None:
        """Switches the current player from X to O, or vice versa."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def update_game_state(self) -> None:
        """
        Checks the board for a win or draw and updates the game state.
        """
        if self._check_win():
            self.game_state = "WIN"
        elif all(cell is not None for cell in self.board):
            self.game_state = "DRAW"
        else:
            self.game_state = "RUNNING"

    def _check_win(self) -> bool:
        """
        Checks if the current player has won.

        Returns:
            bool: True if the current player has won, False otherwise.
        """
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)             # Diagonal
        ]
        for condition in win_conditions:
            if all(self.board[i] == self.current_player for i in condition):
                return True
        return False

    def get_valid_moves(self) -> List[int]:
        """
        Gets a list of all available moves.

        Returns:
            List[int]: A list of integers representing the available positions.
        """
        return [i for i, cell in enumerate(self.board) if cell is None]

class TicTacToeConsole:
    """
    Handles the console interface for the Tic-Tac-Toe game.
    """

    def __init__(self) -> None:
        """Initializes the console game."""
        self.game = TicTacToe()

    def draw_board(self) -> None:
        """Draws the current game board to the console."""
        self.clear_screen()
        board = [cell if cell is not None else ' ' for cell in self.game.board]
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("---|---|---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---|---|---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")

    def get_player_move(self) -> int:
        """
        Prompts the current player for their move.

        Returns:
            int: The position the player chose.
        """
        while True:
            try:
                choice = int(input(f"Player {self.game.current_player}, enter your move (1-9): "))
                if 1 <= choice <= 9 and self.game.board[choice - 1] is None:
                    return choice - 1
                else:
                    print("Invalid move. Please choose an empty cell from 1 to 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_computer_move(self) -> int:
        """
        Determines the computer's move.

        Returns:
            int: The position the computer chose.
        """
        print(f"Computer ({self.game.current_player}) is thinking...")
        time.sleep(1)
        return random.choice(self.game.get_valid_moves())

    def play_pvp(self) -> None:
        """Handles the player vs. player game loop."""
        self.game = TicTacToe()
        while self.game.game_state == "RUNNING":
            self.draw_board()
            move = self.get_player_move()
            self.game.make_move(move)

        self.draw_board()
        self.display_result()

    def play_pvc(self) -> None:
        """Handles the player vs. computer game loop."""
        self.game = TicTacToe()
        while self.game.game_state == "RUNNING":
            self.draw_board()
            move = self.get_player_move() if self.game.current_player == "X" else self.get_computer_move()
            self.game.make_move(move)

        self.draw_board()
        self.display_result()

    def display_result(self) -> None:
        """Displays the final result of the game."""
        if self.game.game_state == "WIN":
            print(f"Player {self.game.current_player} wins!")
        elif self.game.game_state == "DRAW":
            print("It's a draw!")

    @staticmethod
    def clear_screen() -> None:
        """Clears the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

def main() -> None:
    """Main function to run the Tic-Tac-Toe game."""
    console = TicTacToeConsole()
    while True:
        console.clear_screen()
        print("--- Tic-Tac-Toe ---")
        print("1. Player vs Player")
        print("2. Player vs Computer")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            console.play_pvp()
        elif choice == '2':
            console.play_pvc()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()