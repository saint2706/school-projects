from collections import Counter

def get_hand_rank(hand):
    """
    Evaluates a 7-card hand and returns its rank.
    """
    ranks = "23456789TJQKA"

    # We can have multiple hands of 5 cards from the 7 cards available.
    # We need to find the best possible 5-card hand.
    # For simplicity, we will evaluate all 7 cards together first to find pairs, etc.
    # A full implementation would check all 21 combinations of 5 cards.

    all_ranks = sorted([card.rank for card in hand], key=lambda r: ranks.index(r))
    all_suits = [card.suit for card in hand]

    rank_counts = Counter(all_ranks)
    suit_counts = Counter(all_suits)

    is_flush = max(suit_counts.values()) >= 5
    is_straight = False

    # Check for straight
    unique_ranks = sorted(list(set(all_ranks)), key=lambda r: ranks.index(r))
    if len(unique_ranks) >= 5:
        for i in range(len(unique_ranks) - 4):
            # Check for Ace-low straight
            if "A" in unique_ranks and "2" in unique_ranks and "3" in unique_ranks and "4" in unique_ranks and "5" in unique_ranks:
                is_straight = True
                break

            # Check for other straights
            if ranks.index(unique_ranks[i+4]) - ranks.index(unique_ranks[i]) == 4:
                is_straight = True
                break

    # --- Hand Rankings ---
    if is_straight and is_flush:
        # For simplicity, we are not distinguishing between royal and straight flush here.
        return "Straight Flush"

    if 4 in rank_counts.values():
        return "Four of a Kind"

    if 3 in rank_counts.values() and 2 in rank_counts.values():
        return "Full House"

    if is_flush:
        return "Flush"

    if is_straight:
        return "Straight"

    if 3 in rank_counts.values():
        return "Three of a Kind"

    if list(rank_counts.values()).count(2) >= 2:
        return "Two Pair"

    if 2 in rank_counts.values():
        return "One Pair"

    return "High Card"
