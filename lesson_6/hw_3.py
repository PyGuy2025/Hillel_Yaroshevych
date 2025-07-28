user_number = int(input("Enter a number: "))

while user_number > 9:
    result = 1
    for num in str(user_number):
        result *= int(num)
    user_number = result

print(user_number)