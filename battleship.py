import random

class Board:
    """
    Represents the game board.
    """
    def __init__(self, size=10):
        self.size = size
        self.grid = [["O"] * size for _ in range(size)]
        self.ships = []
        self.shots = set()

    def print_board(self, show_ships=False):
        """Prints the game board."""
        print("  " + " ".join(str(i) for i in range(self.size)))
        for r in range(self.size):
            row_str = chr(ord('A') + r) + " "
            for c in range(self.size):
                if not show_ships and (r, c) not in self.shots:
                    row_str += "O "
                elif (r, c) in self.shots:
                    if self.grid[r][c] == "X":
                        row_str += "X "
                    else:
                        row_str += "M "
                elif show_ships and self.grid[r][c] == "S":
                    row_str += "S "
                else:
                    row_str += "O "
            print(row_str)

    def place_ships(self, ship_sizes):
        """Places ships on the board."""
        for size in ship_sizes:
            placed = False
            while not placed:
                orientation = random.choice(["horizontal", "vertical"])
                if orientation == "horizontal":
                    row = random.randint(0, self.size - 1)
                    col = random.randint(0, self.size - size)
                    if all(self.grid[row][c] == "O" for c in range(col, col + size)):
                        for c in range(col, col + size):
                            self.grid[row][c] = "S"
                        self.ships.append([(row, c) for c in range(col, col + size)])
                        placed = True
                else: # vertical
                    row = random.randint(0, self.size - size)
                    col = random.randint(0, self.size - 1)
                    if all(self.grid[r][col] == "O" for r in range(row, row + size)):
                        for r in range(row, row + size):
                            self.grid[r][col] = "S"
                        self.ships.append([(r, col) for r in range(row, row + size)])
                        placed = True

    def take_shot(self, row, col):
        """Takes a shot at a given location."""
        if (row, col) in self.shots:
            return "already_shot"

        self.shots.add((row, col))

        if self.grid[row][col] == "S":
            self.grid[row][col] = "X"
            return "hit"
        else:
            return "miss"

class Game:
    """
    Represents a game of Battleship.
    """
    def __init__(self, board_size=10, ship_sizes=[5, 4, 3, 3, 2], num_shots=30):
        self.board = Board(board_size)
        self.ship_sizes = ship_sizes
        self.num_shots = num_shots
        self.shots_taken = 0

    def play(self):
        """Main function to play the game."""
        self.board.place_ships(self.ship_sizes)

        print("Welcome to Battleship!")
        print(f"You have {self.num_shots} shots to sink all the ships.")

        while self.shots_taken < self.num_shots:
            self.board.print_board()
            print(f"Shots left: {self.num_shots - self.shots_taken}")

            try:
                shot_str = input("Enter your shot (e.g., A5): ").upper()
                if len(shot_str) < 2 or not shot_str[0].isalpha() or not shot_str[1:].isdigit():
                    print("Invalid input. Please use the format A5.")
                    continue

                row = ord(shot_str[0]) - ord('A')
                col = int(shot_str[1:])

                if not (0 <= row < self.board.size and 0 <= col < self.board.size):
                    print("Coordinates are out of bounds.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Please use the format A5.")
                continue

            result = self.board.take_shot(row, col)

            if result == "already_shot":
                print("You've already shot there. Try again.")
            elif result == "hit":
                print("It's a hit!")
                self.shots_taken += 1
            elif result == "miss":
                print("It's a miss.")
                self.shots_taken += 1

            if self.check_win():
                print("You've sunk all the ships! You win!")
                self.board.print_board(show_ships=True)
                return

        print("You're out of shots! You lose.")
        self.board.print_board(show_ships=True)

    def check_win(self):
        """Checks if all ships have been sunk."""
        for ship in self.board.ships:
            for part in ship:
                if self.board.grid[part[0]][part[1]] == "S":
                    return False
        return True

if __name__ == "__main__":
    game = Game()
    game.play()
