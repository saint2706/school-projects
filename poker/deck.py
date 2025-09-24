import random

class Card:
    """
    Represents a playing card with a suit and a rank.
    """
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """
    Represents a deck of 52 playing cards.
    """
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck of cards."""
        random.shuffle(self.cards)

    def deal(self):
        """Deals a single card from the top of the deck."""
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
