from .player import Player

class Team:
    """
    Represents a team in the FIFA game.
    """
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.score = 0

    def __str__(self):
        return self.name
