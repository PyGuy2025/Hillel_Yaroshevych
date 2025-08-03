def find_unique_value(some_list:list) -> int | float :
    counter = {}
    for n in some_list:
        if n in counter:
            counter[n] += 1
        else:
            counter[n] = 1
    for n in some_list:
        if counter[n] == 1:
            return n

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")



"""как я вижу, в модуле collections есть метод Counter и реализовать функцию можно было бы проще:
from collections import Counter
def find_unique_value(some_list:list) -> int | float :
    count_dict = Counter(some_list)
    for n in some_list:
        if count_dict[n] == 1:
            return n
"""