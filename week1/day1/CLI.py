# Write a Python script that:

# Asks the user: "Enter the hostname of the server to deploy: " and saves it to a variable.
# Asks the user: "Enter the target port number: " and saves it to a variable.
# Casts the port number into an integer (to make sure it's a valid numerical port).
# Prints a professional provisioning report using an f-string that looks exactly like this:
# [STATUS] Deploying web server '[hostname]' to port [port_number]...
hostname = input("Enter the hostname of the server to deploy: ")
port_number = input("Enter the target port number: ")
port_number = int(port_number)
print(f"[STATUS] Deploying web server '{hostname}' to port {port_number}")