import sys

first_num = float(input("Your welcome to calculate 2 different numbers. Start with the first number: "))
op = input("Choose your operator: '+', '-', '*', '/': ")
second_num = float(input("And your second number: "))

if op == '+':
    result = first_num + second_num
elif op == '-':
    result = first_num - second_num
elif op == '*':
    result = first_num * second_num
elif op == '/':
    if second_num == 0:
        print("Sorry, but you can't divide by zero")
        result = None
    else:
        result = first_num / second_num
else:
    print("Sorry, but probably you didn't input numbers or right operator")
    result = None

if result is not None:
    print(f"Your answer is: {result}")