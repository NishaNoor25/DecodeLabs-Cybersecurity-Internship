import re
SUSPICIOUS_KEYWORDS = [
    "urgent", "immediate action", "account suspended", "password expires",
    "verify your account", "wire transfer", "strictly confidential",
    "billing failed", "unusual activity", "unauthorized login", "click here",
    "update payment", "security alert", "failed subscription"
]

DANGEROUS_EXTENSIONS = [".iso", ".js", ".scr", ".exe", ".vbs", ".bat", ".ise", ".zip"]

def analyze_email_headers(sender: str, reply_to: str = "") -> list:
    red_flags = []
    
    if "gmail.com" in sender.lower() or "yahoo.com" in sender.lower() or "hotmail.com" in sender.lower():
        if any(role in sender.lower() for role in ["support", "admin", "ceo", "security", "hr"]):
            red_flags.append("Red Flag: Sender-Domain Mismatch (Official entity using free email provider).")
            
    if reply_to and reply_to.lower() != sender.lower():
        red_flags.append(f"Red Flag: Mismatched Return-Path/Reply-To address ({reply_to}).")
        
    return red_flags

def analyze_urls_and_domains(text: str) -> list:
    red_flags = []
    urls = re.findall(r'https?://[^\s]+', text)
    
    for url in urls:
        if any(word in url.lower() for word in ["secure-login", "update", "verify", "login-", "account-"]):
            red_flags.append(f"Red Flag: Combosquatting / Suspicious Subdomain Trap detected in URL: {url}")
        if re.search(r'amaz0n|paypa1|micros0ft|g00gle', url, re.IGNORECASE):
            red_flags.append(f"Red Flag: Typosquatting detected in URL: {url}")
            
    return red_flags

def evaluate_phishing_threat(sender: str, subject: str, body: str, attachment: str = "", reply_to: str = ""):
    red_flags = []
    score = 0
    
    header_flags = analyze_email_headers(sender, reply_to)
    red_flags.extend(header_flags)
    score += len(header_flags) * 2
    
    combined_text = (subject + " " + body).lower()
    found_keywords = [kw for kw in SUSPICIOUS_KEYWORDS if kw in combined_text]
    
    if found_keywords:
        red_flags.append(f"Red Flag: High-pressure cognitive triggers/keywords found: {', '.join(found_keywords)}")
        score += len(found_keywords)
        
    url_flags = analyze_urls_and_domains(body)
    red_flags.extend(url_flags)
    score += len(url_flags) * 2
    
    if attachment:
        for ext in DANGEROUS_EXTENSIONS:
            if attachment.lower().endswith(ext):
                red_flags.append(f"Red Flag: Highly dangerous attachment detected ({attachment}).")
                score += 3
                
    if score == 0:
        triage_status = "SAFE 🟢"
        action = "Action: Close Ticket (No threat detected)."
    elif 1 <= score <= 3:
        triage_status = "SUSPICIOUS 🟡"
        action = "Action: Warn User (Exercise caution, verify out-of-band)."
    else:
        triage_status = "MALICIOUS 🔴"
        action = "Action: Block Domain & Escalate (Purge threat from all inboxes)."
        
    return triage_status, action, red_flags

def main():
    print("==================================================")
    print("  DecodeLabs: Phishing Awareness & Triage Engine  ")
    print("==================================================")
    
    while True:
        print("\n--- Enter Email Details To Analyze ---")
        sender = input("Sender Address (e.g., support@paypal.com): ").strip()
        subject = input("Subject Line: ").strip()
        body = input("Email Body / Text: ").strip()
        attachment = input("Attachment Name (Press Enter if none): ").strip()
        reply_to = input("Reply-To Address (Press Enter if none): ").strip()
        
        status, action, flags = evaluate_phishing_threat(sender, subject, body, attachment, reply_to)
        print("\n" + "="*50)
        print(f"TRIAGE STATUS: {status}")
        print(f"ACTION REQUIRED: {action}")
        print("="*50)
        print("\n[Identified Red Flags]:")
        if flags:
            for flag in flags:
                print(f"- {flag}")
        else:
            print("- None (Email appears legitimate).")
        print("="*50)
         cont = input("\nDo you want to analyze another email? (Y/N): ").strip().upper()
        if cont != 'Y':
            print("\nExiting Phishing Triage Engine. Goodbye!")
            break
        if __name__ == "__main__":
    main()
