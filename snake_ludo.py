import random
import time

class SnakeLudo:
    """
    Represents a simple game of Snake Ludo.
    """
    def __init__(self):
        self.snakes = {13: 7, 17: 7}
        self.players = []
        self.winning_score = 20

    def setup_players(self):
        """Gets the number of players and their names."""
        while True:
            try:
                num_players = int(input("Enter the number of players: "))
                if num_players > 0:
                    break
                else:
                    print("Number of players must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        for i in range(num_players):
            name = input(f"Enter name of player {i+1}: ")
            self.players.append({'name': name, 'position': 0})

    def play(self):
        """Main function to play the game."""
        print("--- Welcome to Snake Ludo ---")
        print("First to reach 20 wins!")
        self.setup_players()

        while True:
            for player in self.players:
                print(f"\n--- {player['name']}'s turn ---")
                input("Press enter to roll...")

                roll = random.randint(0, 5)
                print(f"{player['name']} rolled a {roll}")

                player['position'] += roll

                if player['position'] in self.snakes:
                    print(f"Oh no! You landed on a snake at {player['position']}.")
                    player['position'] = self.snakes[player['position']]
                    print(f"You go down to {player['position']}.")

                print(f"{player['name']}'s new position is {player['position']}")

                if player['position'] >= self.winning_score:
                    print(f"\n--- {player['name']} wins! ---")
                    return

if __name__ == "__main__":
    game = SnakeLudo()
    game.play()
    print("\nThanks for playing!")
