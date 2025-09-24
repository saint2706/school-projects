import random
import time

class BoardGame:
    """
    Represents a simple board game.
    """
    def __init__(self):
        self.position = 0
        self.money = 0
        self.board = {
            1: {'desc': 'The game begins. Rs.0', 'money': 0},
            2: {'desc': '+ Rs.10', 'money': 10},
            3: {'desc': '+ Rs.40', 'money': 40},
            4: {'desc': '- Rs.10', 'money': -10},
            5: {'desc': '+ Rs.50', 'money': 50},
            6: {'desc': 'Oops! Move back to block 1', 'position': 1},
            7: {'desc': '+ Rs.10', 'money': 10},
            8: {'desc': '- Rs.30', 'money': -30},
            9: {'desc': '+ Rs.50', 'money': 50},
            10: {'desc': 'You get another throw!', 'special': 'reroll'},
            11: {'desc': '+ Rs.50', 'money': 50},
            12: {'desc': '+ Rs.30', 'money': 30},
            13: {'desc': '+ Rs.30', 'money': 30},
            14: {'desc': '- Rs.50', 'money': -50},
            15: {'desc': '+ Rs.30', 'money': 30},
            16: {'desc': '+ Rs.30', 'money': 30},
            17: {'desc': '- Rs.50', 'money': -50},
            18: {'desc': '+ Rs.50', 'money': 50},
            19: {'desc': '+ Rs.50', 'money': 50},
            20: {'desc': 'Oops! Move back to block 15!', 'position': 15},
            21: {'desc': '+ Rs.90', 'money': 90},
            22: {'desc': '+ Rs.90', 'money': 90},
            23: {'desc': 'You get another throw!', 'special': 'reroll'},
            24: {'desc': '+ Rs.60', 'money': 60},
            25: {'desc': '- Rs.50', 'money': -50},
            26: {'desc': 'You reached the goal', 'special': 'win'}
        }

    def print_board_layout(self):
        """Prints the layout of the board."""
        num = 1
        for i in range(5):
            for j in range(5):
                if num <= 9:
                    print(num, end='  ')
                else:
                    print(num, end=' ')
                num += 1
            print()
        print("\n" * 3)

    def play(self):
        """Main function to play the game."""
        print('If you have more than Rs.100 in the end, you win!!')
        print('Ready ?')
        time.sleep(2)
        self.print_board_layout()

        while True:
            ch = input('Enter \'y\' to continue or \'e\' to exit: ')
            if ch.lower() != 'y':
                break

            if self.position >= 26:
                print("You've already reached the end!")
                break

            roll = random.randint(1, 6)
            print('Rolling...')
            time.sleep(1)
            print(f'You got {roll}')

            self.position += roll

            if self.position > 26:
                print('You reached the end')
                break

            square = self.board.get(self.position)

            if square:
                print(square['desc'])
                if 'money' in square:
                    self.money += square['money']
                if 'position' in square:
                    self.position = square['position']
                if 'special' in square and square['special'] == 'reroll':
                    print("You get another throw!")
                    continue

            print(f'You are at block {self.position}')
            print(f'You have Rs.{self.money}')
            print("\n" * 2)

        if self.money > 100:
            print('\n\nYou won!! Congrats!')
        else:
            print('\n\nYou lose!!.... Better luck next time!')

        print('\n\nThank you for playing!')


if __name__ == "__main__":
    game = BoardGame()
    game.play()
