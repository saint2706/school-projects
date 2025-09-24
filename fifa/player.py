class Player:
    """
    Represents a player in the FIFA game.
    """
    def __init__(self, name, position, stamina=100):
        self.name = name
        self.position = position
        self.stamina = stamina

    def __str__(self):
        return f"{self.name} ({self.position})"
