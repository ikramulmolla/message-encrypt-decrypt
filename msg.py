def encrypt(text, shift):
    """Encrypt the text using Caesar Cipher with the given shift value."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """Decrypt the text using Caesar Cipher with the given shift value."""
    return encrypt(text, -shift)

def main():
    print("Welcome to the CaesarCipherTool")
    print("This tool was created by Ikramul Molla.")
    print()

    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt? (Enter Q to quit): ").upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        if choice in ['E', 'D']:
            message = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'E':
                result = encrypt(message, shift)
                print(f"Encrypted Message: {result}")
            else:
                result = decrypt(message, shift)
                print(f"Decrypted Message: {result}")
        else:
            print("Invalid choice. Please choose (E) or (D) or Q to quit.")

if __name__ == "__main__":
    main()
