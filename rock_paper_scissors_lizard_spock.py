import random

# --- Game Data ---
CHOICES = ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']

# Defines the winning relationships
WINNING_RULES = {
    'ROCK': ['SCISSORS', 'LIZARD'],
    'PAPER': ['ROCK', 'SPOCK'],
    'SCISSORS': ['PAPER', 'LIZARD'],
    'LIZARD': ['SPOCK', 'PAPER'],
    'SPOCK': ['SCISSORS', 'ROCK']
}

# --- Game Functions ---
def get_player_choice():
    """Gets the player's choice and validates it."""
    while True:
        player_choice = input(f"Enter your choice ({', '.join(CHOICES)}): ").upper()
        if player_choice in CHOICES:
            return player_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    """Gets the computer's choice."""
    return random.choice(CHOICES)

def determine_winner(player_choice, computer_choice):
    """
    Determines the winner of a round.

    Returns:
        str: 'player', 'computer', or 'draw'
    """
    if player_choice == computer_choice:
        return 'draw'
    elif computer_choice in WINNING_RULES[player_choice]:
        return 'player'
    else:
        return 'computer'

def print_rules():
    """Prints the rules of the game."""
    print('''Rules:
    - Scissors cuts Paper
    - Paper covers Rock
    - Rock crushes Lizard
    - Lizard poisons Spock
    - Spock smashes Scissors
    - Scissors decapitates Lizard
    - Lizard eats Paper
    - Paper disproves Spock
    - Spock vaporizes Rock
    - Rock crushes Scissors
    ''')

def play_game():
    """Main function to play the game."""
    print_rules()

    player_name = input('Enter your username: ')

    while True:
        try:
            num_rounds = int(input('Enter the number of rounds: '))
            break
        except ValueError:
            print("Invalid number of rounds. Please enter a number.")

    player_score = 0
    computer_score = 0

    for i in range(num_rounds):
        print(f"\n--- Round {i+1} ---")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f'{player_name} chose {player_choice}, Computer chose {computer_choice}')

        winner = determine_winner(player_choice, computer_choice)
        if winner == 'player':
            print(f'{player_name} wins this round!')
            player_score += 1
        elif winner == 'computer':
            print('Computer wins this round!')
            computer_score += 1
        else:
            print("It's a draw!")

    print("\n--- Final Score ---")
    print(f"{player_name}: {player_score}")
    print(f"Computer: {computer_score}")

    if player_score > computer_score:
        print(f"\n{player_name} wins the game!")
    elif computer_score > player_score:
        print("\nComputer wins the game!")
    else:
        print("\nThe game is a draw!")


if __name__ == "__main__":
    play_game()
