import random
import string

def generate_password(length):
    """
    Generates a random password of a given length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: The generated password.
    """
    chars = string.ascii_letters + string.digits + '@!#$%&'
    return "".join(random.choice(chars) for _ in range(length))

def get_password_strength(length):
    """
    Determines the strength of a password based on its length.

    Args:
        length (int): The length of the password.

    Returns:
        str: The strength of the password.
    """
    if length <= 4:
        return 'Weak'
    elif length <= 6:
        return 'Medium'
    elif length <= 8:
        return 'Strong'
    else:
        return 'Extreme'

def main():
    """
    Main function to run the password generator.
    """
    print("--- Password Generator ---")

    while True:
        try:
            length = int(input('Enter a password length: '))
            if length <= 0:
                print("Password length must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid length. Please enter a number.")

    print("\nHere are 3 generated passwords:")
    for _ in range(3):
        password = generate_password(length)
        print(password)

    strength = get_password_strength(length)
    print(f"\nPassword Level: {strength}")

if __name__ == "__main__":
    main()
