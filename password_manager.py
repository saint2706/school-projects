import random
import string

class PasswordManager:
    """
    A simple password manager that can generate, store, change, and verify passwords.
    """
    def __init__(self):
        self.passwords = {}

    def generate_password(self, length, chars):
        """Generates a random password."""
        return "".join(random.choice(chars) for _ in range(length))

    def add_password(self):
        """Adds a new password for a user."""
        username = input("Enter a username: ")

        use_custom_chars = input("Use custom characters for the password? (yes/no): ").lower()
        if use_custom_chars == 'yes':
            chars = input("Enter the characters to use: ")
        else:
            chars = string.ascii_letters + string.digits + '!@#$%&'

        while True:
            try:
                length = int(input("Enter the password length: "))
                if length <= 0:
                    print("Length must be a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid length. Please enter a number.")

        password = self.generate_password(length, chars)
        self.passwords[username] = password
        print(f"Password for {username} has been generated and stored.")

    def change_password(self):
        """Changes the password for a user."""
        username = input("Enter the username for which you would like to change the password: ")
        if username in self.passwords:
            new_password = input("Enter a new password: ")
            self.passwords[username] = new_password
            print("Password changed successfully.")
        else:
            print("Username not found.")

    def verify_password(self):
        """Verifies the password for a user."""
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in self.passwords and self.passwords[username] == password:
            print("Correct password entered.")
        else:
            print("Incorrect username or password.")

    def main_menu(self):
        """Displays the main menu and handles user choices."""
        while True:
            print("\n--- Password Manager ---")
            print("1. Add a new password")
            print("2. Change a password")
            print("3. Verify a password")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_password()
            elif choice == '2':
                self.change_password()
            elif choice == '3':
                self.verify_password()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = PasswordManager()
    manager.main_menu()
    print("\nThank you for using the Password Manager!")
