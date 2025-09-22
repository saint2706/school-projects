import random

def get_player_choice():
    """Gets the player's choice and validates it."""
    while True:
        player_choice = input("Rock, Paper, Scissors? ").capitalize()
        if player_choice in ["Rock", "Paper", "Scissors"]:
            return player_choice
        else:
            print("That's not a valid play. Check your spelling!")

def get_computer_choice():
    """Gets the computer's choice."""
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(player, computer):
    """Determines the winner of a round."""
    if player == computer:
        return "Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return f"You win! {player} beats {computer}."
    else:
        return f"You lose! {computer} beats {player}."

def play_game():
    """Main function to play the Rock, Paper, Scissors game."""
    try:
        num_rounds = int(input('Enter the number of rounds to play: '))
    except ValueError:
        print("Invalid number of rounds. Please enter a number.")
        return

    for i in range(num_rounds):
        print(f"\n--- Round {i+1} ---")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {player_choice}, computer chose {computer_choice}.")
        print(determine_winner(player_choice, computer_choice))

def main():
    """Main function to run the game."""
    while True:
        play_game()
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
