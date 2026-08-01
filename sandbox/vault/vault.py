import os

def load_vault():
    vault = {}
    if os.path.exists("vault.txt"):
        with open("vault.txt", "r") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    service = parts[0]
                    secret = parts[1]
                    vault[service] = secret
        print("[INFO] Existing vault database loaded from disk.")
    return vault

def add_secret(vault):
    service = input("Enter server/service name: ")
    secret = input("Enter secret key/password: ")
    vault[service] = secret
    print("[SUCCESS] Secret saved successfully in-memory.")

def retrieve_secret(vault):
    service = input("Enter service name to look up: ")
    if service in vault:
        print(f"The secret key is: {vault[service]}")
    else:
        print("Error: Service not found in vault.")

def audit_secret(vault):
    print("\n--- PASSWORD SECURITY AUDIT ---")
    for service, secret in vault.items():
        if len(secret) < 8:
            print(f"[WARNING] Service '{service}' has a WEAK password! (Less than 8 characters)")
        else:
            print(f"[OK] Service '{service}' password strength is secure.")
    print("--------------------------------")

def save_vault(vault):
    with open("vault.txt", "w") as f:
        for service, secret in vault.items():
            f.write(f"{service}:{secret}\n")
    print("[SUCCESS] Vault database successfully saved to disk (vault.txt).")

def run_vault():
    # Load existing data on bootup
    vault = load_vault()
    
    while True:
        print("\n=== SRE LOCAL SECRETS VAULT ===")
        print("[1] Save a New Secret")
        print("[2] Retrieve a Secret")
        print("[3] Audit Passwords Security")
        print("[4] Save & Exit")
        
        choice = input("Enter choice (1-4): ")
        
        # Safe string comparisons (No-crash architecture)
        if choice == "1":
            add_secret(vault)
        elif choice == "2":
            retrieve_secret(vault)
        elif choice == "3":
            audit_secret(vault)
        elif choice == "4":
            save_vault(vault)
            print("Exiting Vault. Stay secure!")
            break
        else:
            print("Invalid Choice. Enter 1-4.")

if __name__ == "__main__":
    run_vault()