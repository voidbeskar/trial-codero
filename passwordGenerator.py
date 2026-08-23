import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Panjang password (default 12): ") or 12)
    except ValueError:
        length = 12

    use_upper = input("Guna huruf besar? (y/n, default y): ").lower() != 'n'
    use_digits = input("Guna angka? (y/n, default y): ").lower() != 'n'
    use_symbols = input("Guna simbol? (y/n, default y): ").lower() != 'n'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\nPassword anda: {password}")

if __name__ == "__main__":
    main()