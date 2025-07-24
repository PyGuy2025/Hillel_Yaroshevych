from keyword import kwlist
from string import punctuation

symb_list = list(punctuation.replace('_', '') + ' ')
numbers = list(range(0, 10))

users_hash = input("Print your hashtag: ")

if (
    all(not c.isupper() for c in users_hash) # check uppers, but keep in mind '_'
    and users_hash not in kwlist # check system words
    and not users_hash[0].isdigit() # check first symbol for digit reqs
    and not any(el in users_hash for el in symb_list) # check punctuation
    and "__" not in users_hash # check for double underscores
):
    print(True)
else:
    print(False)
