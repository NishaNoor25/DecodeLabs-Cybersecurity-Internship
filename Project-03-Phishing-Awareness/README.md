# 🛡️ Project 3: Phishing Awareness & Triage Engine

Welcome to **Project 3** of the **DecodeLabs Industrial Cybersecurity Internship Track**. This project focuses on threat identification, email header analysis, detecting social engineering indicators, and automated phishing triage workflows[cite: 2].

---

## 📋 Overview

The modern cybersecurity perimeter relies heavily on the human firewall. Technical controls alone cannot prevent high-pressure social engineering tactics like Business Email Compromise (BEC), typosquatting, and domain spoofing[cite: 2].

This project implements an **Automated Phishing Triage Engine** that parses email headers, inspects embedded URLs, evaluates psychological urgency triggers, and categorizes incoming threats into actionable decision outcomes (`SAFE 🟢`, `SUSPICIOUS 🟡`, `MALICIOUS 🔴`)[cite: 2].

---

## ✨ Key Technical Features

* **Header & Domain Anomaly Detection:** Identifies display name mismatches, free-provider official impersonation, and return-path spoofing[cite: 2].

* **URL & Subdomain Analysis:** Flags typosquatting (`paypa1`, `amaz0n`) and suspicious subdomain traps (`secure-login`, `verify`)[cite: 2].

* **Cognitive Trigger Parsing:** Evaluates high-pressure psychological keywords exploitation (Urgency, Fear, Authority, Financial)[cite: 2].

* **Malicious File Attachment Inspection:** Detects dangerous executable and smuggling file extensions (`.iso`, `.js`, `.exe`, `.ise`)[cite: 2].

* **Decision Tree Triage Routing:** Automatically maps threat severity scores to standard SOC actions (Close Ticket, Warn User, or Block Domain & Escalate)[cite: 2].

---

## 💻 How to Run

1. **Clone or Download the Repository:**

   git clone https://github.com/NishaNoor25/DecodeLabs-Cybersecurity-Internship.git

2. **Navigate to Project 3 Folder:**

   cd Project-03-Phishing-Awareness

3. **Execute the Python Script:**

   python phishing_analyzer.py

4. **Follow Interactive Prompts:**

   Enter the target email's Sender, Subject, Body, and Attachment details to dynamically generate a live threat assessment and red flag breakdown[cite: 2].


## 🛠️ Tech Stack & Skills

* **Language:** Python 3 (Standard Libraries & Regular Expressions `re`)[cite: 2]

* **Security Concepts:** Threat Analysis, Social Engineering Detection, Email Security, SOC Triage Workflows

**Author:** Nisha Noor

**Track:** Junior Cybersecurity Analyst @ DecodeLabs[cite: 2]
