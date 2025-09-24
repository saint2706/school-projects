import random
import time
import matplotlib.pyplot as plt
from colorama import Fore, Style

class Board:
    """
    Represents the Snakes and Ladders board.
    """
    def __init__(self):
        self.snakes_and_ladders = {
            2: 38, 16: 6, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44,
            46: 25, 49: 11, 51: 67, 62: 19, 64: 60, 71: 91, 74: 53,
            78: 98, 87: 94, 89: 68, 92: 88, 95: 75, 99: 80
        }

    def show_grid(self, players):
        """Displays the game board with players."""
        plt.figure()
        for start, end in self.snakes_and_ladders.items():
            x = [(start % 10 - 1) * 10, (end % 10 - 1) * 10]
            if start % 10 == 0:
                x[0] = 90
            if end % 10 == 0:
                x[1] = 90

            y = [(start // 10) * 10, (end // 10) * 10]
            if start % 10 == 0:
                y[0] = (start // 10 - 1) * 10
            if end % 10 == 0:
                y[1] = (end // 10 - 1) * 10

            color = 'g' if end > start else 'm'
            plt.plot(x, y, c=color)

        for j in range(11):
            x = [(j * 10) - 5 for _ in range(11)]
            y = [10 * i - 5 for i in range(11)]
            y1 = [(j * 10) - 5 for _ in range(11)]
            x1 = [i * 10 - 5 for i in range(11)]
            plt.plot(x, y, c='k')
            plt.plot(x1, y1, c='k')

        plt.yticks([10 * i for i in range(10)], [10 * (i) for i in range(1, 11)])
        plt.xticks([10 * i for i in range(10)], [i for i in range(1, 11)])

        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        for i, player in enumerate(players):
            pos = player['position']
            xc = (pos % 10 - 1) * 10 if pos % 10 != 0 else 90
            yc = (pos // 10) * 10 if pos % 10 != 0 else (pos // 10 - 1) * 10
            plt.scatter(xc, yc, c=colors[i], s=100, label=player['name'])

        plt.title('(っ◔◡◔)っ ♥ Snakes and Ladders ♥')
        plt.legend()
        plt.show()

class Game:
    """
    Manages the Snakes and Ladders game flow.
    """
    def __init__(self):
        self.board = Board()
        self.players = []
        self.game_over = False

    def setup_players(self):
        """Gets the number of players and their names."""
        while True:
            try:
                num_players = int(input('Enter number of players (minimum 2 and maximum 7): '))
                if 2 <= num_players <= 7:
                    break
                else:
                    print('Invalid number of players. Please enter a number between 2 and 7.')
            except ValueError:
                print('Invalid input. Please enter a number.')

        colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
        for i in range(num_players):
            name = input(f'Enter name of player {i+1}: ')
            self.players.append({'name': name, 'position': 0, 'color': colors[i]})
            print(f"{name}'s color is {colors[i]}")

    def play(self):
        """Main function to play the game."""
        self.setup_players()

        while not self.game_over:
            for i, player in enumerate(self.players):
                print(f"\n--- {player['name']}'s turn ---")
                action = input('Press enter to roll or q to quit: ')
                if action.lower() == 'q':
                    self.game_over = True
                    break

                roll = random.randint(1, 6)
                print(f"{player['name']} rolled a {roll}")

                if roll == 6:
                    print(Fore.GREEN + f"{player['name']} rolled a six! You get to roll again." + Style.RESET_ALL)
                    roll += random.randint(1, 6)
                    print(f"{player['name']} rolled another {roll-6}, for a total of {roll}")

                player['position'] += roll

                if player['position'] > 100:
                    player['position'] -= roll
                    print(Fore.RED + "You can't go past 100!" + Style.RESET_ALL)
                elif player['position'] == 100:
                    print(Fore.GREEN + f"{player['name']} has won the game!" + Style.RESET_ALL)
                    self.game_over = True
                    break
                elif player['position'] in self.board.snakes_and_ladders:
                    new_pos = self.board.snakes_and_ladders[player['position']]
                    if new_pos > player['position']:
                        print(Fore.GREEN + f"You found a ladder! You climb from {player['position']} to {new_pos}." + Style.RESET_ALL)
                    else:
                        print(Fore.MAGENTA + f"You were bitten by a snake! You slide from {player['position']} to {new_pos}." + Style.RESET_ALL)
                    player['position'] = new_pos

                print(f"{player['name']}'s new position is {player['position']}")
                self.board.show_grid(self.players)

        print("\n--- Game Over ---")
        print("Thanks for playing!")

if __name__ == "__main__":
    game = Game()
    game.play()
