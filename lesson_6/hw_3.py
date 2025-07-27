user_number = int(input("Enter a number: "))

while user_number > 9:
    result = 1
    for _ in str(user_number):
        result *= int(_)
    user_number = result

print(user_number)