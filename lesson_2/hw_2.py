number = int(input("Введіть 5-значне число: "))

d1 = number % 10
number = number // 10

d2 = number % 10
number = number // 10

d3 = number % 10
number = number // 10

d4 = number % 10
number = number // 10

d5 = number

reversed_number = d1 * 10000 + d2 * 1000 + d3 * 100 + d4 * 10 + d5

print(reversed_number)