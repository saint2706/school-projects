import random
from colorama import Fore, Style

def print_house_map(player_location=None):
    """
    Prints the map of the house, with an indicator for the player's location.

    Args:
        player_location (str, optional): The room the player is currently in. Defaults to None.
    """
    house_map = [
        '____________________________________________________________',
        '                              |                            |',
        '                              |                            |',
        '                              |                            |',
        '    KITCHEN                   |                            |',
        '                              |                            |',
        '                              |         LIVING             |',
        '______________________________|          ROOM              |',
        '                              |                            |',
        '                              |                            |',
        '                              |                            |',
        '                              |                            |',
        '                              |                            |',
        '                              |                            |',
        '     BEDROOM                  |                            |',
        '                              |                            |',
        '                              |______________--------______|',
        '                              |          |     DOOR',
        '                              |          |      ** ',
        '                              |          | you are here',
        '                              | STORE    |',
        '______________________________| ROOM     |',
        '                              |          |',
        '                              |          |',
        '                              |          |',
        '   WASHROOM                   |          |',
        '                              |          |',
        '                              |          |',
        '                              |          |',
        '______________________________|__________|'
    ]

    locations = {
        "KITCHEN": (4, 4),
        "LIVING ROOM": (6, 40),
        "BEDROOM": (14, 5),
        "STORE ROOM": (21, 35),
        "WASHROOM": (25, 3)
    }

    if player_location and player_location in locations:
        x, y = locations[player_location]
        # Clear the default "you are here"
        house_map[19] = '                              |          |'
        # Place the player marker
        line = list(house_map[x])
        line[y:y+2] = "**"
        house_map[x] = "".join(line)
        line = list(house_map[x+1])
        line[y-2:y+12] = "you are here"
        house_map[x+1] = "".join(line)

    print("\n".join(house_map))

def play_game():
    """
    Main function to play the guess the room game.
    """
    print('THIS IS A HOUSE. THERE IS PRIZE HIDDEN IN ONE OF THE ROOMS.')
    print('ALL YOU GOTTA DO IS GUESS THE ROOM IN WHICH THE PRIZE IS HIDDEN.')
    print('YOU HAVE 3 CHANCES TO GUESS THE ROOM BEFORE YOU LOSE. WATCH OUT FOR THE CHANCEMETER AND GOOD LUCK!')

    rooms = ['KITCHEN', 'STORE ROOM', 'LIVING ROOM', 'WASHROOM', 'BEDROOM']
    correct_room = random.choice(rooms)
    chances = 3

    while chances > 0:
        print_house_map()
        print(f'CHANCES LEFT: {chances}')

        try:
            guess = input('ENTER YOUR GUESS: ').upper()
        except EOFError:
            print("\nQuitting game.")
            break

        if guess not in rooms:
            print(Fore.YELLOW + "That's not a valid room. Please choose from: " + ", ".join(rooms))
            print(Style.RESET_ALL)
            continue

        if guess == correct_room:
            print(Fore.GREEN + 'SPECTACULAR GUESSING SKILLS!! ACHIEVEMENT UNLOCKED "GUESS LEVEL = 100"')
            print(Style.RESET_ALL)
            break
        else:
            chances -= 1
            print(Fore.BLUE + 'Wrong Guess Mate, Try Again:')
            print(Style.RESET_ALL)
            if chances > 0:
                print_house_map(guess)
            else:
                print(Fore.RED + 'OOPS SORRY, YOU LOST!')
                print(Style.RESET_ALL)

    print(Fore.MAGENTA + f'{correct_room} was the correct room MR.SHERLOCK')
    print(Style.RESET_ALL)
    input("Press Enter to exit...")


if __name__ == "__main__":
    play_game()
