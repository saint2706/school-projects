from .deck import Deck
from .player import Player
from .hand_evaluator import get_hand_rank

class Game:
    """
    Represents a game of Texas Hold'em poker.
    """
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.deck = Deck()
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0

    def play(self):
        """
        Main function to play a round of poker.
        """
        print("--- New Round ---")
        self.deck.shuffle()
        self._deal_hole_cards()

        self._betting_round()
        self._deal_flop()
        self._betting_round()
        self._deal_turn()
        self._betting_round()
        self._deal_river()
        self._betting_round()

        self._showdown()

    def _deal_hole_cards(self):
        """Deals two hole cards to each player."""
        print("--- Dealing Hole Cards ---")
        for _ in range(2):
            for player in self.players:
                player.hand.append(self.deck.deal())

        for player in self.players:
            print(f"{player.name}'s hand: [{player.hand[0]}, {player.hand[1]}]")

    def _deal_flop(self):
        """Deals the flop (first three community cards)."""
        print("--- Dealing Flop ---")
        self.community_cards.extend([self.deck.deal() for _ in range(3)])
        self._print_community_cards()

    def _deal_turn(self):
        """Deals the turn (fourth community card)."""
        print("--- Dealing Turn ---")
        self.community_cards.append(self.deck.deal())
        self._print_community_cards()

    def _deal_river(self):
        """Deals the river (fifth community card)."""
        print("--- Dealing River ---")
        self.community_cards.append(self.deck.deal())
        self._print_community_cards()

    def _print_community_cards(self):
        """Prints the community cards."""
        print("Community cards: ", ", ".join(str(card) for card in self.community_cards))

    def _betting_round(self):
        """Manages a round of betting."""
        print("--- Betting Round ---")
        for player in self.players:
            if not player.is_folded:
                self._get_player_action(player)

    def _get_player_action(self, player):
        """Gets the action from a player."""
        while True:
            try:
                action = input(f"{player.name}, what would you like to do? (bet, call, raise, fold, check): ").lower()

                if action == "fold":
                    player.fold()
                    break
                elif action == "check":
                    if player.current_bet < self.current_bet:
                        print("You can't check, you need to call the current bet.")
                    else:
                        break
                elif action == "call":
                    amount_to_call = self.current_bet - player.current_bet
                    if player.call(amount_to_call):
                        self.pot += amount_to_call
                        break
                elif action == "bet":
                    amount = int(input("Enter bet amount: "))
                    if player.bet(amount):
                        self.pot += amount
                        self.current_bet = player.current_bet
                        break
                elif action == "raise":
                    amount = int(input("Enter raise amount: "))
                    if player.raise_bet(amount, self.current_bet):
                        self.pot += (player.current_bet - self.current_bet)
                        self.current_bet = player.current_bet
                        break
                else:
                    print("Invalid action.")
            except ValueError:
                print("Invalid input. Please enter a number for bet/raise amount.")

    def _showdown(self):
        """
        Determines the winner of the round.
        """
        print("--- Showdown ---")
        best_hand_rank = -1
        winner = None

        hand_ranks = ["High Card", "One Pair", "Two Pair", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush"]

        for player in self.players:
            if not player.is_folded:
                full_hand = player.hand + self.community_cards
                hand_rank_str = get_hand_rank(full_hand)
                hand_rank = hand_ranks.index(hand_rank_str)

                print(f"{player.name} has a {hand_rank_str}")

                if hand_rank > best_hand_rank:
                    best_hand_rank = hand_rank
                    winner = player

        if winner:
            print(f"\n--- {winner.name} wins the round with a {hand_ranks[best_hand_rank]}! ---")
            winner.money += self.pot
        else:
            print("No winner could be determined.")
