# Write a script that asks the user for a number (e.g. 5), and then prints its multiplication table from 1 to 10.
# Expected Output for number 5:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
n = int(input("Enter the number to generate its table: "))
for i in range(1,11):
    print(f" {n} X {i} = {n*i}")
