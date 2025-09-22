from .game import Game

def main():
    """
    Main function to run the poker game.
    """
    player_names = ["Player 1", "Player 2"] # Can be expanded to get names from user input
    game = Game(player_names)
    game.play()

if __name__ == "__main__":
    main()
