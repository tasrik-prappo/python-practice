import random
import string

chars: list = list(" " + string.punctuation + string.digits + string.ascii_letters)
key: list = chars.copy()

random.shuffle(key)

original_message: str = input("Enter the message: ")
encrypted_message: str = ""

for letter in original_message:

    index: int = chars.index(letter)
    encrypted_message += key[index]

print(f"Encrypted message: {encrypted_message}")

original_message = ""
encrypted_message = input("Enter the encrypted message: ")

for letter in encrypted_message:

    index: int = key.index(letter)
    original_message += chars[index]

print(f"Original message: {original_message}")