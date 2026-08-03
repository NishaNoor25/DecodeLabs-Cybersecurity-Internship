Project 1: Password Strength Checker

📋 Overview

Project 1 is the defensive phase of the DecodeLabs track. Before sensitive user credentials reach cryptographic hashing or database storage, they must pass strict data validation. This tool evaluates authentication risk through pure string-handling, pattern recognition, and conditional logic.

✨ Key Features

O(n) Linear Time Complexity: Built using Pythonic short-circuit evaluation for high-performance execution.

Leaked / Compromised Password Lookup: Cross-references user inputs against a database of known weak/breached credentials (e.g., admin123, 12345678).

Rule Enforcement & Entropy Check:

Enforces minimum length (8+ characters).

Checks for Uppercase Letters (A-Z).

Checks for Digits (0-9).

Checks for Special Symbols (!@#$%^&*).

Interactive CLI Loop: Allows continuous password evaluations in the terminal without restarting execution (Y/N user prompt).

💻 How to Run

Clone or Download this Repository:

Download the zip file of this repository or clone it using git:

git clone https://github.com/NishaNoor25/DecodeLabs-Cybersecurity-Internship.git

Navigate to the Project Folder:
Open your command prompt or terminal and move to the folder:

cd DecodeLabs-Cybersecurity-Internship

Run the Script:
Execute the script using Python:

python password_checker.py
Follow the On-Screen Prompts:

Enter the password you want to evaluate and interactively check multiple passwords as prompted.

🛠️ Tech Stack & Skills

Language: Python 3

Core Concepts: Defensive Logic, Data Validation, String Handling, Time Complexity Optimization.

Author: Nisha Noor

Track: intern at DecodeLabs
