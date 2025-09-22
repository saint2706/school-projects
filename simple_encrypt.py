def encrypt(message):
    """
    Encrypts a message using a simple character code manipulation.
    """
    sol = ''
    for char in message:
        y = ord(char)
        if y <= 50:
            p = y - 10
            sol += chr(p)
        elif 50 < y <= 75:
            q = y + 25
            sol += chr(q)
        elif 75 < y <= 100:
            r = y + 200
            sol += chr(r)
        elif 100 < y <= 200:
            s = y + 1000
            sol += chr(s)
    return sol

def decrypt(message):
    """
    Decrypts a message that was encrypted with the encrypt function.
    """
    ans = ''
    for char in message:
        z = ord(char)
        if -10 <= z <= 40:
            a = z + 10
            ans += chr(a)
        elif 75 < z <= 100:
            b = z - 25
            ans += chr(b)
        elif 275 < z <= 300:
            c = z - 200
            ans += chr(c)
        elif 1100 < z <= 1200:
            d = z - 1000
            ans += chr(d)
    return ans

def main():
    """
    Main function to run the encryption/decryption tool.
    """
    while True:
        choice = input("Would you like to encrypt or decrypt a message? (encrypt/decrypt/quit): ").lower()

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
