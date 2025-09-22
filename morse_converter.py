# --- Morse Code and Custom Cipher Converter ---

MORSE_CODE_DICT = { 'A':'•―', 'B':'―•••', 'C':'―•―•', 'D':'―••', 'E':'•',
                    'F':'••―•', 'G':'― ―•', 'H':'••••', 'I':'••', 'J':'•― ― ―',
                    'K':'―•―', 'L':'•―••', 'M':'― ―', 'N':'―•', 'O':'― ― ―',
                    'P':'•― ―•', 'Q':'― ―•―', 'R':'•―•', 'S':'•••', 'T':'―',
                    'U':'••―', 'V':'•••―', 'W':'•― ―', 'X':'―••―', 'Y':'―•― ―',
                    'Z':'― ―••', '1':'•― ― ― ―', '2':'••― ― ―', '3':'•••― ― ―',
                    '4':'••••―', '5':'•••••', '6':'―••••', '7':'― ―•••',
                    '8':'― ― ―••', '9':'― ― ― ―•', '0':'― ― ― ― ―', ', ':'--..--',
                    '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

CUSTOM_CIPHER_DICT = {'A':',:,','B':'.*.','C':'{%{','D':'"<"','E':')()','F':':::',
                      'G':';:;','H':'*]*','I':'!_!','J':'^_^','K':'&','L':'@^5','M':'$,?','N':'#|#',
                      'O':'[|[','P':'`~`','Q':'~`~','R':'>2.','S':',*<','T':'+-+','U':'?|?','V':':_=',
                      'W':'.!.','X':'$:^','Y':';@#','Z':',.?',
                      'a':'|#5','b':'0$|','c':'%,8','d':'[91','e':'&=-','f':'*&9','g':'(18',
                      'h':'O_0','i':':\:','j':'@@@','k':'8&%','l':'5,2','m':'7&5','n':'89(','o':'||<',
                      'p':'$|Y','q':'!@1','r':'&h(','s':'i*&','t':'5/6','u':'*^5','v':'#/r',
                      'w':'pU6','x':';.[','y':'))(','z':';-+',
                      '1':'L<.','2':'H//{','3':'*&&','4':'LK8','5':'_--','6':'{=+}','7':'#;0',
                      '8':'?p]','9':'i+5','0':'@!+',
                      '!':',,.','&':'oo0','(':'p&+',")":'+._','$':'>>?',' ':'98z'}

def encrypt(message, cipher_dict):
    """
    Encrypts a message using the selected cipher.
    """
    cipher = ''
    for letter in message:
        if letter in cipher_dict:
            cipher += cipher_dict[letter]
        else:
            cipher += ' ' # Keep spaces as they are
    return cipher

def decrypt(message, cipher_dict):
    """
    Decrypts a message from the selected cipher into English.
    """
    reversed_cipher_dict = {v: k for k, v in cipher_dict.items()}

    # Custom cipher uses 3-character codes
    if cipher_dict == CUSTOM_CIPHER_DICT:
        decipher = ''
        i = 0
        while i < len(message):
            code = message[i:i+3]
            if code in reversed_cipher_dict:
                decipher += reversed_cipher_dict[code]
                i += 3
            else:
                decipher += ' '
                i += 1
        return decipher
    else: # Morse code
        message += ' '
        decipher = ''
        citext = ''
        for letter in message:
            if (letter != ' '):
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2 :
                    decipher += ' '
                else:
                    if citext in reversed_cipher_dict:
                        decipher += reversed_cipher_dict[citext]
                    citext = ''
        return decipher

def main():
    """
    Main function to run the converter.
    """
    while True:
        cipher_choice = input("Choose a cipher (morse/custom) or 'quit': ").lower()
        if cipher_choice == 'quit':
            break

        if cipher_choice == 'morse':
            cipher_dict = MORSE_CODE_DICT
        elif cipher_choice == 'custom':
            cipher_dict = CUSTOM_CIPHER_DICT
        else:
            print("Invalid choice. Please choose 'morse' or 'custom'.")
            continue

        mode = input("Would you like to encrypt or decrypt a message? (encrypt/decrypt): ").lower()

        if mode == 'encrypt':
            message = input("Enter the message to encrypt: ").upper()
            result = encrypt(message, cipher_dict)
            print(f"Encrypted message: {result}")
        elif mode == 'decrypt':
            message = input("Enter the message to decrypt: ")
            result = decrypt(message, cipher_dict)
            print(f"Decrypted message: {result}")
        else:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
