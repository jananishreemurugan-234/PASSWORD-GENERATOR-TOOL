import random
import string

# Optional clipboard support
try:
    import pyperclip
    clipboard_support = True
except ImportError:
    clipboard_support = False
    print("Clipboard support not available. Install with: pip install pyperclip")

def generate_password(length, include_digits, include_special):
    # Base character pool (letters)
    character_pool = string.ascii_letters

    if include_digits:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    # Generate password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def save_password_to_file(password):
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")

def main():
    try:
        length = int(input("Enter password length: "))
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'
    except ValueError:
        print("Invalid input. Please enter valid data.")
        return

    password = generate_password(length, include_digits, include_special)
    print("\nGenerated Password:", password)

    # Save to file
    save_password_to_file(password)
    print("Password saved to passwords.txt")

    # Copy to clipboard if available
    if clipboard_support:
        pyperclip.copy(password)
        print("Password copied to clipboard!")

if __name__ == "__main__":
    main()