import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# Load or generate salt
if not os.path.exists("salt.key"):
    with open("salt.key", "wb") as f:
        f.write(os.urandom(16))

with open("salt.key", "rb") as f:
    salt = f.read()

# Derive key from master password
master_pwd = input("Master password: ")

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100_000,
)
key = base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))
fer = Fernet(key)


def view():
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                user, enc_pwd = line.strip().split("|")
                print(
                    f"User: {user} | Password: {fer.decrypt(enc_pwd.encode()).decode()}"
                )
    except Exception as e:
        print("Error:", e)


def add():
    user = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(f"{user}|{fer.encrypt(pwd.encode()).decode()}\n")


while True:
    mode = input("Add or view passwords? (add/view), q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid choice.")
