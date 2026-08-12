
# 🛡️ Project 2: Basic Encryption & Decryption Engine (Caesar Cipher)

Welcome to **Project 2** of the **DecodeLabs Industrial Cybersecurity Internship Track**. This project focuses on fundamental cryptographic transformations, data confidentiality, and mathematical obfuscation mechanisms.

---

## 📋 Overview

Data in transit across open networks is inherently vulnerable to interception.

This project implements a **Symmetric Encryption & Decryption Engine** utilizing the classic **Caesar Cipher mechanism**.

By applying modular arithmetic (% 26) and integer ASCII mapping (`ord()` / `chr()`), raw text (plaintext) is rendered completely unreadable to unauthorized eyes before being reversed back into its original state.

---

## ✨ Key Technical Features

* **Custom Shift Key Logic:** Allows flexible integer shift keys (n) for dynamic encryption and decryption routines.
* **Modular Arithmetic Wrap-Around (% 26):** Ensures characters naturally cycle through the 26-letter English alphabet without indexing errors.
* **Character Case & Edge Case Preservation:** Preserves Uppercase (A-Z), Lowercase (a-z), spaces, numbers, and special symbols without altering structural context.
* **Interactive CLI Workflows:** Features continuous user loop handling and full mathematical reversal checks for complete verification.



## 💻 How to Run

1. **Clone or Download the Repository:**
git clone [https://github.com/NishaNoor25/DecodeLabs-Cybersecurity-Internship.git](https://www.google.com/search?q=https://github.com/NishaNoor25/DecodeLabs-Cybersecurity-Internship.git)
2. **Navigate to Project 2 Folder:**
cd DecodeLabs-Cybersecurity-Internship/Project-02-Caesar-Cipher
3. **Execute the Python Script:**
python caesar_cipher.py
4. **Follow On-Screen Execution Prompts:**
Choose your preferred option (1 for Encryption, 2 for Decryption, 3 for Demonstration) and enter your custom shift key when prompted.


## 🛠️ Tech Stack & Skills

* **Language:** Python 3 (Standard Libraries)
* **Cryptographic Concepts:** Symmetric Encryption, Data Confidentiality, Caesar Cipher Mechanics, Modular Arithmetic, ASCII Transformations.





**Author:** Nisha Noor

**Track:** Junior Cybersecurity Analyst @ DecodeLabs


