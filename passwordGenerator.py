import argparse
import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    char_pool = ''
    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("No character types selected. Please choose at least one character type.")

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument('-l', '--length', type=int, required=True, help="Length of the password")
    parser.add_argument('--letters', action='store_true', help="Include letters in the password")
    parser.add_argument('--numbers', action='store_true', help="Include numbers in the password")
    parser.add_argument('--symbols', action='store_true', help="Include symbols in the password")

    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.letters, args.numbers, args.symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
