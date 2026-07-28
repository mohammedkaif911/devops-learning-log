# Creates a variable available_ram and sets it to the string "8".
# Converts (casts) available_ram into an integer so you can do math with it.
# Calculates how much extra RAM you have above your safety threshold and prints a message like: "We have [extra_ram] GB of extra safe memory!"
threshold = 4
available_ram = "8"
available_ram = int(available_ram)
safe_ram = available_ram - threshold
print(f"We have {safe_ram} GB of extra safe memory")