def sum_of_digits(n):
    result = ""
    sum = 0
    if n < 10:
        return n
    
    
    return n%10 + sum_of_digits(n // 10)
user_num = int(input("Enter a number: "))
print(sum_of_digits(user_num))