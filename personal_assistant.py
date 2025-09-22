import random

# --- Data for the assistant ---
JOKES = [
    "My sister and I often laugh about how competitive we are.\nBut I laugh more.",
    "If we shouldn’t eat at night, why do they put a light in the fridge?",
    "Velcro - What a rip off!",
    "Don't you hate it when someone answers their own questions?\nI do",
    "So what if I don't know what Armageddon means?\nIt's not the end of the world..."
]

MAGIC_8_BALL_RESPONSES = [
    'It is certain.',
    'It is decidedly so.',
    'Signs point to yes.',
    'Yes - definitely.',
    'Cannot predict now.',
    'Try again later.',
    "Don't count on it",
    'It is highly doubtful.'
]

def tell_joke():
    """Prints a random joke."""
    print(random.choice(JOKES))

def magic_8_ball():
    """Acts as a magic 8-ball."""
    input('Ask a question: ')
    print(random.choice(MAGIC_8_BALL_RESPONSES))

def spin_the_wheel():
    """Spins a wheel with user-defined choices."""
    try:
        num_choices = int(input('Enter the number of choices: '))
        choices = []
        for i in range(num_choices):
            choice = input(f'Enter choice {i+1}: ')
            choices.append(choice)

        if choices:
            print(f'The choice selected is: {random.choice(choices)}')
        else:
            print("No choices were entered.")

    except ValueError:
        print("Invalid number of choices. Please enter a number.")

def print_help():
    """Prints the help menu."""
    print("\n--- Kōkua's Functions ---")
    print("  - 'joke': Tells you a joke.")
    print("  - 'decide': Helps you make a decision (Magic 8-Ball).")
    print("  - 'spin': Spins a wheel with your choices.")
    print("  - 'help': Shows this help menu.")
    print("  - 'bye': Exits the assistant.")
    print("-------------------------\n")

def main():
    """Main function for the personal assistant."""
    print('Hi! I am Kōkua! Your Personal assistant! :}')
    print('It is my duty to make your life as convenient as possible.')
    print_help()

    commands = {
        "joke": tell_joke,
        "decide": magic_8_ball,
        "spin": spin_the_wheel,
        "help": print_help
    }

    while True:
        try:
            inp = input('How can I help you? ').lower()
        except EOFError:
            print("\nBye! It was my pleasure serving you...")
            break

        if inp == 'bye':
            print('Bye! It was my pleasure serving you...')
            break

        if inp in commands:
            commands[inp]()
        else:
            print("I don't understand that command. Type 'help' for a list of functions.")

if __name__ == "__main__":
    main()
