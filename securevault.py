import json
import os
import random
import string
from cryptography.fernet import Fernet
from colorama import init, Fore, Back, Style

init()

def generate_key():
    return Fernet.generate_key()

def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

def generate_secure_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_passwords(passwords, file_name='passwords.json'):
    with open(file_name, 'w') as f:
        json.dump(passwords, f, indent=4)

def load_passwords(file_name='passwords.json'):
    if not os.path.exists(file_name):
        return {}
    with open(file_name, 'r') as f:
        return json.load(f)

def display_ascii_art():
    print(Fore.BLUE + '''
//////////////////////////////////////
//╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╦  ╦┌─┐┬ ┬┬ ┌┬┐ //
//╚═╗├┤ │  │ │├┬┘├┤ ╚╗╔╝├─┤│ ││  │  //
//╚═╝└─┘└─┘└─┘┴└─└─┘ ╚╝ ┴ ┴└─┘┴─┘┴  //
//////////////////////////////////////
''' + Style.RESET_ALL)

def show_menu():
    print(Fore.GREEN + "Welcome to SecureVault" + Style.RESET_ALL)
    print("1. Add a new password")
    print("2. View a password")
    print("3. Delete a password")
    print("4. Generate a secure password")
    print("5. Exit")

def main():
    display_ascii_art()
    key = None
    if os.path.exists("key.key"):
        with open("key.key", 'rb') as key_file:
            key = key_file.read()
    else:
        key = generate_key()
        with open("key.key", 'wb') as key_file:
            key_file.write(key)
    
    passwords = load_passwords()
    
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            site = input("Enter the site name: ").strip()
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            encrypted_password = encrypt_password(password, key)
            passwords[site] = {
                'username': username,
                'password': encrypted_password.decode()
            }
            save_passwords(passwords)
            print(Fore.CYAN + "Password saved successfully!" + Style.RESET_ALL)

        elif choice == '2':
            site = input("Enter the site name to view password: ").strip()
            if site in passwords:
                decrypted_password = decrypt_password(passwords[site]['password'].encode(), key)
                print(Fore.YELLOW + f"Username: {passwords[site]['username']}" + Style.RESET_ALL)
                print(Fore.YELLOW + f"Password: {decrypted_password}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Site not found!" + Style.RESET_ALL)

        elif choice == '3':
            site = input("Enter the site name to delete: ").strip()
            if site in passwords:
                del passwords[site]
                save_passwords(passwords)
                print(Fore.RED + "Password deleted successfully!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Site not found!" + Style.RESET_ALL)

        elif choice == '4':
            length = int(input("Enter the length of the password (default is 16): ").strip() or 16)
            generated_password = generate_secure_password(length)
            print(Fore.GREEN + f"Generated password: {generated_password}" + Style.RESET_ALL)

        elif choice == '5':
            print(Fore.BLUE + "Exiting SecureVault. Stay safe!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid option. Please choose between 1-5." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
