import random
import time
import os
import json

# --- Constants ---
COLORS = {'RED': 'R', 'YELLOW': 'Y', 'ORANGE': 'O', 'GREEN': 'G', 'BLUE': 'B', 'PURPLE': 'P'}
COLOR_LIST = list(COLORS.values())
TITLE_CARD = '''
               *     *    *    *****  *******  ******  *****  *     *  *******  *     *  * * *
               * * * *   * *   *         *     *       *   *  * * * *     *     * *   *  *    *
               *  *  *  *****  *****     *     ******  *****  *  *  *     *     *  *  *  *    *
               *     *  *   *      *     *     *       * *    *     *     *     *   * *  *    *
               *     *  *   *  *****     *     ******  *   *  *     *  *******  *     *  * * *
                                                                                       V-1

                                            BY AAYUSH RAJESH                                        '''

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_rules():
    """Prints the rules of the game."""
    print('RULES:')
    print('1.The Player will attempt to guess the code set by the Challenger/Computer within a certain number of tries')
    print('   Easy-     12 tries')
    print('   Medium-   10 tries ')
    print('   Difficult-8 tries')
    print('2.There are 6 colours to choose from')
    print('   RED-   R     YELLOW-Y')
    print('   ORANGE-O     GREEN- G')
    print('   BLUE-  B     PURPLE-P')
    print('A feedback will be provided after every move')

def get_difficulty():
    """Gets the difficulty level from the user and returns the number of tries."""
    while True:
        mode = input('Enter difficulty level- Easy, Medium or Difficult: ').upper()
        if mode == 'EASY':
            return 12
        elif mode == 'MEDIUM':
            return 10
        elif mode == 'DIFFICULT':
            return 8
        else:
            print('Not a valid mode. Please enter again')

def get_code(opponent):
    """Gets the secret code from the challenger or computer."""
    if opponent == 'CHALLENGER':
        while True:
            code = input('Enter the 6 colour code Challenger, with the colour codes: ').upper()
            if len(code) != 6:
                print('Code must be 6 characters long. Try again.')
                continue
            if all(char in COLOR_LIST for char in code):
                return code
            else:
                print('Code does not follow the colour codes. Try again.')
    else: # COMPUTER
        code = "".join(random.choices(COLOR_LIST, k=6))
        print('Computer has set the code.')
        return code

def play_game():
    """Main function to play the Mastermind game."""
    clear_screen()
    print(TITLE_CARD)
    print_rules()

    num_tries = get_difficulty()

    while True:
        opponent = input('Enter your opponent- Challenger or Computer: ').upper()
        if opponent in ['CHALLENGER', 'COMPUTER']:
            break
        else:
            print('Not a valid opponent. Please enter again.')

    secret_code = get_code(opponent)
    clear_screen()

    print(TITLE_CARD)
    print("\nKEY:")
    print(json.dumps(COLORS, indent=3))

    tries = 1
    while tries <= num_tries:
        print(f"\n--- Try {tries}/{num_tries} ---")

        guess = input('Enter your guess: ').upper()

        if len(guess) != 6 or not all(char in COLOR_LIST for char in guess):
            print('Invalid guess. Make sure it is 6 characters long and uses valid colors.')
            continue

        if guess == secret_code:
            print("\nCongratulations! You've guessed the code!")
            break

        correct_position = 0
        correct_color = 0

        temp_secret = list(secret_code)
        temp_guess = list(guess)

        # First pass: check for correct color in correct position
        for i in range(len(temp_guess)):
            if temp_guess[i] == temp_secret[i]:
                correct_position += 1
                temp_secret[i] = None # Mark as checked
                temp_guess[i] = None # Mark as checked

        # Second pass: check for correct color in wrong position
        for i in range(len(temp_guess)):
            if temp_guess[i] is not None and temp_guess[i] in temp_secret:
                correct_color += 1
                temp_secret[temp_secret.index(temp_guess[i])] = None # Mark as checked

        print("\n--- Feedback ---")
        print(f"Correct color in correct position: {correct_position}")
        print(f"Correct color in wrong position: {correct_color}")

        tries += 1

    if tries > num_tries:
        print(f"\nGame over! You've run out of tries. The code was: {secret_code}")

def main():
    """Main function to run the Mastermind game."""
    while True:
        play_game()
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
