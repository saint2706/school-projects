import random
import os
import time

class TicTacToe:
    """
    Represents a game of Tic-Tac-Toe.
    """
    def __init__(self):
        self.board = [' ' for _ in range(10)]
        self.player = 1
        self.game_state = "RUNNING"
        self.mark = 'X'

    def draw_board(self):
        """Draws the game board."""
        clear_screen()
        print(" %c | %c | %c " % (self.board[1], self.board[2], self.board[3]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[4], self.board[5], self.board[6]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[7], self.board[8], self.board[9]))
        print("   |   |   ")

    def check_position(self, x):
        """Checks if a position is empty."""
        return self.board[x] == ' '

    def check_win(self):
        """Checks if a player has won."""
        # Horizontal winning condition
        if (self.board[1] == self.board[2] and self.board[2] == self.board[3] and self.board[1] != ' '):
            self.game_state = "WIN"
        elif (self.board[4] == self.board[5] and self.board[5] == self.board[6] and self.board[4] != ' '):
            self.game_state = "WIN"
        elif (self.board[7] == self.board[8] and self.board[8] == self.board[9] and self.board[7] != ' '):
            self.game_state = "WIN"
        # Vertical Winning Condition
        elif (self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[1] != ' '):
            self.game_state = "WIN"
        elif (self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[2] != ' '):
            self.game_state = "WIN"
        elif (self.board[3] == self.board[6] and self.board[6] == self.board[9] and self.board[3] != ' '):
            self.game_state = "WIN"
        # Diagonal Winning Condition
        elif (self.board[1] == self.board[5] and self.board[5] == self.board[9] and self.board[5] != ' '):
            self.game_state = "WIN"
        elif (self.board[3] == self.board[5] and self.board[5] == self.board[7] and self.board[5] != ' '):
            self.game_state = "WIN"
        # Match Tie Condition
        elif all(self.board[i] != ' ' for i in range(1, 10)):
            self.game_state = "DRAW"
        else:
            self.game_state = "RUNNING"

    def play_pvp(self):
        """Player vs Player game mode."""
        while self.game_state == "RUNNING":
            self.draw_board()
            if self.player % 2 != 0:
                print("Player 1's chance")
                self.mark = 'X'
            else:
                print("Player 2's chance")
                self.mark = 'O'

            try:
                choice = int(input("Enter the position between [1-9] where you want to mark: "))
                if choice < 1 or choice > 9:
                    print("Invalid choice. Please enter a number between 1 and 9.")
                    time.sleep(1)
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                time.sleep(1)
                continue

            if self.check_position(choice):
                self.board[choice] = self.mark
                self.player += 1
                self.check_win()

        self.draw_board()
        if self.game_state == "DRAW":
            print("Game Draw")
        elif self.game_state == "WIN":
            self.player -= 1
            if self.player % 2 != 0:
                print("Player 1 Won")
            else:
                print("Player 2 Won")

    def play_pvc(self):
        """Player vs Computer game mode."""
        player_mark, computer_mark = 'X', 'O'

        while self.game_state == "RUNNING":
            self.draw_board()
            print("Player's chance")

            # Player's move
            try:
                choice = int(input("Enter the position between [1-9] where you want to mark: "))
                if choice < 1 or choice > 9:
                    print("Invalid choice. Please enter a number between 1 and 9.")
                    time.sleep(1)
                    continue
                if not self.check_position(choice):
                    print("Position already taken. Try again.")
                    time.sleep(1)
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                time.sleep(1)
                continue

            self.board[choice] = player_mark
            self.check_win()
            if self.game_state != "RUNNING":
                break

            # Computer's move
            self.draw_board()
            print("Computer's chance")
            time.sleep(1)

            # Simple AI: choose a random empty spot
            while True:
                comp_choice = random.randint(1, 9)
                if self.check_position(comp_choice):
                    self.board[comp_choice] = computer_mark
                    break

            self.check_win()

        self.draw_board()
        if self.game_state == "DRAW":
            print("Game Draw")
        elif self.game_state == "WIN":
            if self.mark == player_mark:
                print("Player Won")
            else:
                print("Computer Won")

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main function to run the Tic-Tac-Toe game."""
    while True:
        clear_screen()
        print("--- Tic-Tac-Toe ---")
        print("1. Player vs Player")
        print("2. Player vs Computer")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            game = TicTacToe()
            game.play_pvp()
        elif choice == '2':
            game = TicTacToe()
            game.play_pvc()
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
