import string
import secrets

def generate_password(length, use_punctuation):
    chars = string.ascii_letters + string.digits
    if use_punctuation:
        chars += string.punctuation
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def main():
    print("🔐 Strong Password Generator (Python)")
    print("-------------------------------------")

    while True:
        user_input = input("Enter password length (10 or more): ")
        try:
            length = int(user_input)
            if length < 10:
                print("Length must be at least 10.\n")
            else:
                break
        except ValueError:
            print("Please enter a valid number.\n")

    while True:
        choice = input("Include punctuation for extra strength? (y/n): ").strip().lower()
        if choice in ("y", "n"):
            use_punctuation = (choice == "y")
            break
        else:
            print("Please enter 'y' or 'n'.\n")

    password = generate_password(length, use_punctuation)

    print("\nYour generated password:")
    print("-------------------------------------")
    print(password)
    print("-------------------------------------")

if __name__ == "__main__":
    main()