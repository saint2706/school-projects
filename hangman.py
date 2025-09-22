import random
import time
import os

# --- Graphics ---
GRAPHICS = [
    '''
             ________
             |      |
             |
             |
             |
             |
          ___|_____
    ''',
    '''
             ________
             |      |
             |      O
             |
             |
             |
          ___|_____
    ''',
    '''
             ________
             |      |
             |      O
             |      |
             |      |
             |
          ___|_____
    ''',
    '''
             ________
             |      |
             |      O
             |     /|\\
             |      |
             |
          ___|_____
    ''',
    '''
             ________
             |      |
             |      O
             |     /|\\
             |      |
             |     / \\
          ___|_____
    '''
]

WORDS = ['OUIJA','JAZZ','BAGPIPES','CROQUET','DWARVES','QUILL','CROWD','NEEDLE','GYPSY','CARAVAN','TRACTOR','ALLIGATOR','SPHINX',
         'PHARAOH','GENERAL','ZOMBIE','MEMENTO','FJORD','JUKEBOX','YACHT','GAZEBO','FISHHOOK','ACOUSTIC','ANTHROPOLOGY','MYTHOLOGY',
         'ATMOSPHERE','BLACKBOARD','CENTURY','GOVERNMENT','HELICOPTER','HYDRAULIC','IRONCLAD','MARRIAGE','PALEONTOLOGY','PERMAFROST',
         'PNEUMONOULTRAMICROSCOPICSILICOVOLCANOCONIOSIS','SYZYGY','ASTRONOMY','ZUCCHINI','XYLOPHONE','ZOOLOGIST','WINDSHIELD','ACCORDION',
         'APPENDIX','BASKETBALL','CASSEROLE','CORRESPONDENT','GYMNASTICS','HIPPOPOTAMUS','INCANDESCENCE']

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word(mode):
    """Returns a word for the game, either random or from user input."""
    if mode == '1':
        return random.choice(WORDS)
    else:
        return input("Enter a word for the other player to guess: ").upper()

def display_board(strikes, guessed_letters, word_to_guess):
    """Displays the hangman board."""
    clear_screen()
    print(GRAPHICS[strikes])
    print()

    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)
    print()
    print(f"Strikes: {strikes}/4")
    print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")

def play_game(mode):
    """Main function to play the hangman game."""
    word_to_guess = get_word(mode)
    guessed_letters = set()
    strikes = 0

    while strikes < 4:
        display_board(strikes, guessed_letters, word_to_guess)

        guess = input("Guess a letter or the whole word: ").upper()

        if len(guess) > 1: # Word guess
            if guess == word_to_guess:
                break
            else:
                print("Wrong word guess!")
                strikes += 1
                time.sleep(1)
        elif len(guess) == 1: # Letter guess
            if guess in guessed_letters:
                print("You've already guessed that letter.")
                time.sleep(1)
            elif guess in word_to_guess:
                print("Correct guess!")
                guessed_letters.add(guess)
                time.sleep(1)
            else:
                print("Wrong guess!")
                guessed_letters.add(guess)
                strikes += 1
                time.sleep(1)
        else:
            print("Invalid input.")
            time.sleep(1)

        if all(letter in guessed_letters for letter in word_to_guess):
            break

    display_board(strikes, guessed_letters, word_to_guess)
    if strikes < 4:
        print("\nCongratulations, you won!")
    else:
        print("\nGame over! The word was:", word_to_guess)

def main():
    """Main function to run the hangman game."""
    while True:
        clear_screen()
        print("--- Hangman ---")
        print("1. Play against the computer")
        print("2. Player vs Player")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice in ['1', '2']:
            play_game(choice)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
