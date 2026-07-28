# We import Python's built-in random module.
# We generate a secret number between 1 and 10: secret_number = random.randint(1, 10)
# We ask the user for a guess using input() and cast it to an integer.
# Write the conditional logic:
# If the guess is equal to the secret number, print: "Winner! You guessed the secret number!"
# If the guess is greater than the secret number, print: "Too high! The secret number was [secret_number]"
# If the guess is less than the secret number, print: "Too low! The secret number was [secret_number]"\

import random
secret_n = random.randint(1,10)
n = int(input("Guess the number between 1 to 10: "))
if (n == secret_n):
    print("Winner! You guessed the secret number!")
elif (n>secret_n):
    print(f"Too high! The secret number was {secret_n}")
else:
    print(f"Too low! The secret number was {secret_n}")