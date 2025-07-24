from keyword import kwlist
from string import punctuation

symb_list = list(punctuation.replace('_', '') + ' ')
numbers = list(range(0, 10))

user_input = input("Print your hashtag: ")

if (
    all(not c.isupper() for c in user_input) # check uppers, but keep in mind '_'
    and user_input not in kwlist # check system words
    and not user_input[0].isdigit() # check first symbol for digit reqs
    and not any(el in user_input for el in symb_list) # check punctuation
    and "__" not in user_input # check for double underscores
):
    print(True)
else:
    print(False)
