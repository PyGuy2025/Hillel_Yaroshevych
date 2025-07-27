from string import ascii_letters

users_input = input("Enter two letters separated by '-': ")
first_letter = users_input[0]
second_letter = users_input[-1]

first_index = ascii_letters.index(first_letter)
second_index = ascii_letters.index(second_letter) + 1


result = ascii_letters[first_index:second_index]
print(result)