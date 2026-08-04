
import random

def play_secure_game():
    secret_num = random.randint(1, 10)
    print("=========================================")
    print("★ SRE SECURE NUMBER GUESSER CLI ★")
    print("=========================================\n")
    print("System has generated a secret integer between 1 and 10.")
    
    while True:
        user_input = input("Enter your guess: ")
        
        #THE EXCEPTION-HANDLING SHIELD (Try/Except)
        try:
            # Try to cast the input to an integer
            guess = int(user_input)
        except ValueError:
            # If the user typed garbage, Python raises a ValueError. 
            # We catch it here, block the crash, and continue the loop!
            print("  ⚠️ INPUT ERROR: Invalid non-numeric value! Please enter an integer.")
            continue
            
        # Core Game Logic
        if guess == secret_num:
            print(f"\n[WINNER] Perfect guess! The secret number was indeed {secret_num}!")
            break
        elif guess > secret_num:
            print(f"  -> {guess} is too high! Try again.")
        else:
            print(f"  -> {guess} is too low! Try again.")
            
    print("\n=========================================")

if __name__ == "__main__":
    play_secure_game()