# A simple substitution cipher for encrypting and decrypting messages.

# The key for the substitution cipher
CIPHER_KEY = {
    'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm',
    'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q', 'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w',
    'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c', ' ': '^',
    'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I', 'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M',
    'K': 'N', 'L': 'O', 'M': 'P', 'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U', 'S': 'V', 'T': 'W',
    'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C',
    '1': '0', '2': '9', '3': '8', '4': '7', '5': '6', '6': '5', '7': '4', '8': '3', '9': '2', '0': '1',
    ',': '<', '.': '>', '/': '?', '"': "'", ';': ':', '}': ']', '{': '[', '+': '=', '_': '-',
    ')': '!', '(': '@', '*': '#', '&': '$', '~': '%', '%': '~', '$': '&', '#': '*', '@': '(',
    '!': ')', '<': "'", '>': '.', '?': '/', "'": '"', ':': ';', ']': '}', '[': '{', '=': '+', '-': '_'
}

def encrypt(message):
    """
    Encrypts a message using the substitution cipher.

    Args:
        message (str): The message to encrypt.

    Returns:
        str: The encrypted message.
    """
    encrypted_message = ""
    for char in message:
        if char in CIPHER_KEY:
            encrypted_message += CIPHER_KEY[char]
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message):
    """
    Decrypts a message using the substitution cipher.

    Args:
        message (str): The message to decrypt.

    Returns:
        str: The decrypted message.
    """
    decrypted_message = ""
    # Create a reverse mapping of the cipher key for efficient decryption
    reversed_cipher_key = {v: k for k, v in CIPHER_KEY.items()}

    for char in message:
        if char in reversed_cipher_key:
            decrypted_message += reversed_cipher_key[char]
        else:
            decrypted_message += char
    return decrypted_message

def main():
    """
    Main function to run the encrypt/decrypt tool.
    """
    while True:
        choice = input("Type 'encrypt' to encrypt a message, 'decrypt' to decrypt a message, or 'quit' to exit: ").lower()

        if choice == 'quit':
            break

        if choice in ['encrypt', 'decrypt']:
            message = input("Enter your message: ")
            if choice == 'encrypt':
                result = encrypt(message)
                print(f"Encrypted message: {result}")
            else:
                result = decrypt(message)
                print(f"Decrypted message: {result}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
