import string
import secrets


def Password_generator(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length must be at least 8 characters.")
        return None
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]
    for i in range(length - 4):
        password.append(secrets.choice(all_characters))
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


def main():
    length = int(input("Enter the desired password length: "))
    password = Password_generator(length)
    if password:
        print("Generated Password:", password)


if __name__ == "__main__":
    main()
