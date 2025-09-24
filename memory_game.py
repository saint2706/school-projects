import random
import time

class MemoryGame:
    """
    Represents a memory game where the player finds pairs of symbols.
    """
    def __init__(self):
        self.symbols = ["#", "!", "@", "%", "^", "!", "~", "*", "^", "$", "@", "%", "#", "*", "$", "~"]
        random.shuffle(self.symbols)
        self.board = [" " for _ in range(16)]
        self.chances = 10
        self.matched_pairs = 0

    def print_board(self):
        """Prints the game board."""
        print(" _____ _____ _____ _____ ")
        for i in range(4):
            row = "|"
            for j in range(4):
                index = i * 4 + j
                row += f" {self.board[index]:<2} |"
            print(row)
            print("|_____|_____|_____|_____|")

    def play(self):
        """Main function to play the game."""
        print("--- Memory Game ---")
        print("Find all the pairs of symbols.")
        print(f"You have {self.chances} chances.")

        while self.chances > 0 and self.matched_pairs < 8:
            self.print_board()

            try:
                pos1 = int(input("Enter position 1 (1-16): ")) - 1
                if not (0 <= pos1 < 16) or self.board[pos1] != " ":
                    print("Invalid position. Please choose an empty spot.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            self.board[pos1] = self.symbols[pos1]
            self.print_board()

            try:
                pos2 = int(input("Enter position 2 (1-16): ")) - 1
                if not (0 <= pos2 < 16) or self.board[pos2] != " " or pos1 == pos2:
                    print("Invalid position. Please choose an empty spot.")
                    self.board[pos1] = " "
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                self.board[pos1] = " "
                continue

            self.board[pos2] = self.symbols[pos2]
            self.print_board()

            if self.symbols[pos1] == self.symbols[pos2]:
                print("It's a match!")
                self.matched_pairs += 1
            else:
                print("Not a match. Try again.")
                self.board[pos1] = " "
                self.board[pos2] = " "

            self.chances -= 1
            print(f"\n{self.chances} chances remaining.")
            time.sleep(2)

        if self.matched_pairs == 8:
            print("\nCongratulations! You won!")
        else:
            print("\nGame over! You ran out of chances.")

if __name__ == "__main__":
    game = MemoryGame()
    game.play()
