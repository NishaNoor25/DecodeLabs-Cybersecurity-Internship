# DecodeLabs-Cybersecurity-Internship

Welcome to my repository for the DecodeLabs Industrial Cybersecurity Internship Track.

🚀 Project 1: Password Strength Checker
📋 Overview

Project 1 is the defensive phase of the DecodeLabs track. Before sensitive user credentials reach cryptographic hashing or database storage, they must pass strict data validation. This tool evaluates authentication risk through pure string-handling, pattern recognition, and conditional logic.

 ✨ Features
 
 Linear Time Complexity:** Built using Pythonic short-circuit evaluation (`any()`) for high-performance execution.
Leaked / Compromised Password Lookup:** Cross-references user inputs against a database of known weak/breached credentials (e.g., `admin123`, `12345678`).

Rule Enforcement & Entropy Check:

  - Enforces minimum length ( 8 characters).
  - Checks for Uppercase Letters (`A-Z`).
  - Checks for Digits (`0-9`).
  - Checks for Special Symbols (`!@#$%^&*`).
  Interactive CLI Loop:** Allows continuous password evaluations in the terminal without restarting execution (`Y/N` user prompt).

 💻 How to Run
 
 1. Prerequisites
 2. 
Make sure you have **Python 3.x** installed on your system. No external libraries are required (uses standard built-in modules).

 3. Execution
    
Open your terminal or command prompt, navigate to the project directory, and run:

bash

python password_checker.py

5. Usage Example

Enter any password when prompted.

View the strength evaluation score (Weak 🔴, Medium 🟡, or Strong 🟢).

Type Y to evaluate another password, or N to exit the program.

🛠️ Tech Stack & Skills

Language: Python 3

Core Concepts: Defensive Logic, Data Validation, String Handling, Time Complexity Optimization.

Author: Nisha Noor

Track: @ DecodeLabs
