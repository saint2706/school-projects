import random
from typing import List

class BlackjackGame:
    """
    A class to represent a game of Blackjack.
    """

    def __init__(self):
        """
        Initializes the Blackjack game, setting up the deck and hands.
        """
        self.deck: List[int] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        self.user_cards: List[int] = []
        self.computer_cards: List[int] = []
        self.is_game_over: bool = False

    def _deal_card(self) -> int:
        """
        Deals a single card from the deck.

        Returns:
            int: The value of the card dealt.
        """
        return random.choice(self.deck)

    def _calculate_score(self, cards: List[int]) -> int:
        """
        Calculates the score of a given hand.

        Args:
            cards (List[int]): A list of integers representing the cards in a hand.

        Returns:
            int: The calculated score. Returns 0 for a Blackjack.
        """
        if sum(cards) == 21 and len(cards) == 2:
            return 0  # Blackjack

        # Adjust for Aces
        score = sum(cards)
        num_aces = cards.count(11)
        while score > 21 and num_aces:
            score -= 10
            num_aces -= 1
        return score

    def _compare_scores(self, user_score: int, computer_score: int) -> str:
        """
        Compares the user's and computer's scores to determine the winner.

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
        Main method to run the Blackjack game.
        """
        print("Welcome to Blackjack!")

        # Initial deal
        for _ in range(2):
            self.user_cards.append(self._deal_card())
            self.computer_cards.append(self._deal_card())

        # Main game loop
        while not self.is_game_over:
            user_score = self._calculate_score(self.user_cards)
            computer_score = self._calculate_score(self.computer_cards)

            print(f"    Your cards: {self.user_cards}, current score: {user_score}")
            print(f"    Computer's first card: {self.computer_cards[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                self.is_game_over = True
            else:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_should_deal.lower() == 'y':
                    self.user_cards.append(self._deal_card())
                else:
                    self.is_game_over = True

        # Computer's turn
        computer_score = self._calculate_score(self.computer_cards)
        while computer_score != 0 and computer_score < 17:
            self.computer_cards.append(self._deal_card())
            computer_score = self._calculate_score(self.computer_cards)

        # Final results
        user_score = self._calculate_score(self.user_cards)
        print(f"\n    Your final hand: {self.user_cards}, final score: {user_score}")
        print(f"    Computer's final hand: {self.computer_cards}, final score: {computer_score}")
        print(self._compare_scores(user_score, computer_score))

def main():
    """
    Main function to run the Blackjack game.
    """
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        game = BlackjackGame()
        game.play()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()