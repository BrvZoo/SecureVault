# SecureVault 🔐
![Capture](https://github.com/user-attachments/assets/0e8ef34f-3f35-41aa-8c06-985b77d0f3e7)




Welcome to **SecureVault**, your personal password manager and encryption tool designed to ensure the security and confidentiality of your sensitive data. **SecureVault** allows you to securely store, manage, and generate passwords with ease, using state-of-the-art encryption methods.

## ⚡ Features:
- **Password Management**: Safely store your passwords encrypted with strong encryption.
- **Password Generation**: Generate secure random passwords with letters, numbers, and special characters.
- **Encryption and Decryption**: Your passwords are encrypted using the `cryptography` library’s `Fernet` symmetric encryption, ensuring data confidentiality.
- **Local Storage**: Passwords are stored locally on your machine in an encrypted JSON file, ensuring privacy and security.
- **Easy-to-Use Interface**: Command-line interface that makes it easy to add, view, delete, and generate passwords.

## 🛠 Installation:

To use **SecureVault**, you need to install the required dependencies. Ensure you have Python 3.6 or higher installed, then run the following:

```bash
pip install cryptography colorama
```
**🚀 How to Run:**

1. Clone this repository or download the Python file.
2. Run the application using Python:
```bash
python securevault.py
```
The program will guide you through adding, viewing, deleting, and generating passwords.

## 🔐 Security Features:

1. Encryption
All your passwords are encrypted using Fernet encryption from the cryptography library. This ensures that even if someone gains access to your password file, they won’t be able to read your passwords without the encryption key.

2. Password Generation
SecureVault can generate random, complex passwords with a mix of letters, numbers, and symbols, ensuring your accounts remain secure.

3. Local Storage
Passwords are saved in a local JSON file, ensuring that your sensitive data is never stored on any third-party server or cloud service. Only the encryption key, stored in key.key, can decrypt your data.

4. Encryption Key
A unique encryption key is generated on the first run and stored in a file called key.key. This key is required for both encryption and decryption of passwords. Keep it safe: if you lose the key, you will not be able to decrypt your stored passwords.

## 💡 Usage Example:

Upon running the program, you’ll see a menu with the following options:

1. Add a new password: Enter a website, username, and password to store them securely.
2. View a password: Retrieve a saved password by entering the associated site name.
3. Delete a password: Remove a stored password from the system.
4. Generate a secure password: Generate a random password with customizable length.

## 🔑 Important Security Notes:

1. Backup your key: The key.key file contains the encryption key. If you lose it, your encrypted passwords will be lost forever.
2. Never share key.key: Keep the key in a secure place. Do not upload it to any cloud storage or share it publicly.
3. Password Storage: Passwords are stored in an encrypted form, so even if someone gains access to your passwords.json file, they cannot read your passwords without the decryption key.

## 🤝 Contributing:

Feel free to fork this repository and submit issues or pull requests if you have any ideas for improvements or new features. We welcome contributions to improve the security and functionality of SecureVault.

## 💬 Feedback:

If you encounter any issues or have suggestions for improvement, please open an issue in the GitHub repository, and I’ll be happy to assist!

## 📄 License:

Distributed under the MIT License. See LICENSE for more information.

## Thank you for using SecureVault! Stay safe, and protect your data. 🔐
