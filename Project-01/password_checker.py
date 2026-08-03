import string
COMMON_WEAK_PASSWORDS = [
    "12345678",
    "password",
    "password123",
    "admin123",
    "qwerty1234"
]

def check_password_strength(password: str) -> str:
    # Remove spaces and convert to lowercase for accurate match
    clean_password = password.replace(" ", "").lower()

    if clean_password in COMMON_WEAK_PASSWORDS:
        return "Weak 🔴 [ALERT: This password is in the compromised/leaked list!]"

    if len(password) < 8:
        return "Weak 🔴 (Password must be at least 8 characters long)"
    
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    
    score = sum([has_upper, has_digit, has_symbol])
    
    if score == 3:
        return "Strong 🟢"
    elif score == 2:
        return "Medium 🟡 (Tip: Include a combination of Uppercase, Numbers, and Symbols)"
    else:
        return "Weak 🔴 (Lacks variety: Uppercase, Digits, or Symbols)"

def main():
    print("==================================================")
    print("   DecodeLabs: Password Strength Checker v1.0    ")
    print("==================================================")
    
    while True:
        user_pass = input("\nEnter password to evaluate: ")
        result = check_password_strength(user_pass)
        
        print("-" * 50)
        print(f"Result: {result}")
        print("-" * 50)
        
        choice = input("Do you want to check another password? (Y/N): ").strip().upper()
        
        if choice != 'Y':
            print("\nThank you for using Password Strength Checker. Exiting...")
            break

if __name__ == "__main__":
    main()
