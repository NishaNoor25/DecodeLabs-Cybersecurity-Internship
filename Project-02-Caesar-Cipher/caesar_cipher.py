def encrypt_caesar(plaintext: str, shift: int) -> str:
    """
    Encrypts plaintext using Caesar Cipher logic.
    Formula: E_n(x) = (x + n) % 26
    """
    ciphertext = []
    
    for char in plaintext:
        # Preserve Uppercase Letters (ASCII 65-90)
        if char.isupper():
            shifted = (ord(char) - 65 + shift) % 26 + 65
            ciphertext.append(chr(shifted))
        # Preserve Lowercase Letters (ASCII 97-122)
        elif char.islower():
            shifted = (ord(char) - 97 + shift) % 26 + 97
            ciphertext.append(chr(shifted))
        # Preserve Spaces, Numbers, and Special Characters unchanged
        else:
            ciphertext.append(char)
            
    return "".join(ciphertext)


def decrypt_caesar(ciphertext: str, shift: int) -> str:
    """
    Decrypts ciphertext back to original plaintext using reverse shift logic.
    Formula: D_n(x) = (x - n) % 26
    """
    # Decryption is simply encryption with a negative shift
    return encrypt_caesar(ciphertext, -shift)


def main():
    print("==================================================")
    print("  DecodeLabs: Caesar Cipher Encryption/Decryption ")
    print("==================================================")
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Both (Encrypt & Decrypt Demo)")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '4':
            print("\nExiting Cryptographic Tool. Goodbye!")
            break
            
        if choice in ['1', '2', '3']:
            text = input("\nEnter text: ")
            
            # Input validation for shift key
            try:
                shift_key = int(input("Enter custom shift key (integer, e.g., 3): "))
            except ValueError:
                print("❌ Invalid shift key! Please enter an integer number.")
                continue
                
            if choice == '1':
                encrypted = encrypt_caesar(text, shift_key)
                print("-" * 50)
                print(f"Original Text : {text}")
                print(f"Encrypted Text: {encrypted}")
                print("-" * 50)
                
            elif choice == '2':
                decrypted = decrypt_caesar(text, shift_key)
                print("-" * 50)
                print(f"Encrypted Text: {text}")
                print(f"Decrypted Text: {decrypted}")
                print("-" * 50)
                
            elif choice == '3':
                encrypted = encrypt_caesar(text, shift_key)
                decrypted = decrypt_caesar(encrypted, shift_key)
                print("-" * 50)
                print(f"Original Plaintext : {text}")
                print(f"Ciphertext (Key={shift_key}): {encrypted}")
                print(f"Decrypted Result   : {decrypted}")
                print("-" * 50)
        else:
            print("❌ Invalid option! Please select between 1 and 4.")
            
        cont = input("\nWould you like to process another text? (Y/N): ").strip().upper()
        if cont != 'Y':
            print("\nThank you for using DecodeLabs Cryptographic Engine!")
            break

if __name__ == "__main__":
    main()
