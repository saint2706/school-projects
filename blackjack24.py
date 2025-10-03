"""
A command-line based Blackjack game.

This module implements a simple text-based Blackjack (21) game where the player
competes against the computer. The game follows standard Blackjack rules,
including handling Aces as 1 or 11 and recognizing a Blackjack.

Classes:
    BlackjackGame: Encapsulates the entire logic for a single game of Blackjack.

Functions:
    main: The main entry point to start the game and handle replay logic.

Usage:
    To play the game, run this script from the command line:
    $ python blackjack24.py
"""
import random
from typing import List

class BlackjackGame:
    """
    A class to represent and manage a single game of Blackjack.

    This class handles the deck, player and computer hands, dealing cards,
    calculating scores, and determining the winner.

    Attributes:
        deck (List[int]): A list representing the deck of cards. Aces are 11.
        user_cards (List[int]): The player's current hand.
        computer_cards (List[int]): The computer's current hand.
        is_game_over (bool): A flag to indicate if the game has concluded.
    """

    def __init__(self):
        """
        Initializes the Blackjack game.

        This method sets up a new deck of 52 cards (4 suits), initializes empty
        hands for the player and computer, and sets the game state to not over.
        """
        # A standard 52-card deck with 4 suits. 11 is Ace, 10s are Jack, Queen, King.
        self.deck: List[int] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        self.user_cards: List[int] = []
        self.computer_cards: List[int] = []
        self.is_game_over: bool = False

    def _deal_card(self) -> int:
        """
        Deals a single random card from the deck.

        Returns:
            int: The value of the card dealt.
        """
        # Note: This implementation allows for cards to be reused, simulating an infinite deck.
        return random.choice(self.deck)

    def _calculate_score(self, cards: List[int]) -> int:
        """
        Calculates the score of a given hand, handling Blackjack and Aces.

        A Blackjack (an Ace and a 10-value card) is represented by a score of 0.
        Aces are counted as 11, but if the total score exceeds 21, an Ace's
        value is reduced from 11 to 1.

        Args:
            cards (List[int]): A list of integers representing the cards in a hand.

        Returns:
            int: The calculated score. Returns 0 for a Blackjack.
        """
        # A score of 0 represents a Blackjack (21 with 2 cards).
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        # Adjust for Aces if the score is over 21.
        score = sum(cards)
        num_aces = cards.count(11)
        while score > 21 and num_aces:
            score -= 10  # Change Ace from 11 to 1
            num_aces -= 1
        return score

    def _compare_scores(self, user_score: int, computer_score: int) -> str:
        """
        Compares the user's and computer's scores to determine the game's outcome.

        This method evaluates all possible end-game scenarios, such as draws,
        Blackjacks, busts, and wins based on the higher score.

        Args:
            user_score (int): The user's final score.
            computer_score (int): The computer's final score.

        Returns:
            str: A message indicating the result of the game.
        """
        if user_score == computer_score:
            return "It's a draw."
        elif computer_score == 0:
            return "You lose, opponent has Blackjack."
        elif user_score == 0:
            return "You win with a Blackjack!"
        elif user_score > 21:
            return "You went over. You lose."
        elif computer_score > 21:
            return "Opponent went over. You win."
        elif user_score > computer_score:
            return "You win."
        else:
            return "You lose."

    def play(self):
        """
        Main method to run the Blackjack game from start to finish.

        This method handles the initial deal, the player's turn (hitting or
        standing), the computer's turn, and the final comparison of scores.
        """
        print("Welcome to Blackjack!")

        # Initial deal: two cards to both the player and the computer.
        for _ in range(2):
            self.user_cards.append(self._deal_card())
            self.computer_cards.append(self._deal_card())

        # Main game loop for the player's turn.
        while not self.is_game_over:
            user_score = self._calculate_score(self.user_cards)
            computer_score = self._calculate_score(self.computer_cards)

            print(f"    Your cards: {self.user_cards}, current score: {user_score}")
            print(f"    Computer's first card: {self.computer_cards[0]}")

            # Check for immediate end conditions (Blackjack or bust).
            if user_score == 0 or computer_score == 0 or user_score > 21:
                self.is_game_over = True
            else:
                # Ask the player to hit or stand.
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_should_deal.lower() == 'y':
                    self.user_cards.append(self._deal_card())
                else:
                    self.is_game_over = True

        # Computer's turn: hit until the score is 17 or more.
        computer_score = self._calculate_score(self.computer_cards)
        while computer_score != 0 and computer_score < 17:
            self.computer_cards.append(self._deal_card())
            computer_score = self._calculate_score(self.computer_cards)

        # Final results announcement.
        user_score = self._calculate_score(self.user_cards)
        print(f"\n    Your final hand: {self.user_cards}, final score: {user_score}")
        print(f"    Computer's final hand: {self.computer_cards}, final score: {computer_score}")
        print(self._compare_scores(user_score, computer_score))

def main():
    """
    Main function to run the Blackjack game.

    This function contains the primary loop that allows the user to play
    multiple games of Blackjack without restarting the script.
    """
    # Loop to allow playing multiple games.
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        game = BlackjackGame()
        game.play()
    print("Thanks for playing!")

# This ensures that the main() function is called only when the script is executed directly.
if __name__ == "__main__":
    main()