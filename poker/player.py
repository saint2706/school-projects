class Player:
    """
    Represents a player in the poker game.
    """
    def __init__(self, name, money=1000):
        self.name = name
        self.money = money
        self.hand = []
        self.is_folded = False
        self.current_bet = 0

    def __str__(self):
        return f"{self.name} (${self.money})"

    def fold(self):
        """Folds the player's hand."""
        self.is_folded = True

    def bet(self, amount):
        """Bets a certain amount of money."""
        if amount > self.money:
            print("You can't bet more money than you have.")
            return False

        self.money -= amount
        self.current_bet += amount
        return True

    def call(self, amount_to_call):
        """Calls the current bet."""
        if self.money >= amount_to_call:
            self.money -= amount_to_call
            self.current_bet += amount_to_call
            return True
        else:
            # Player goes all-in
            self.current_bet += self.money
            self.money = 0
            return True

    def raise_bet(self, amount, current_bet):
        """Raises the current bet."""
        total_bet = amount + (current_bet - self.current_bet)
        if total_bet > self.money:
            print("You can't bet more money than you have.")
            return False

        self.money -= total_bet
        self.current_bet += total_bet
        return True
