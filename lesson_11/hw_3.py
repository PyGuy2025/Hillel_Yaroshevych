def is_even(number:int) -> bool:
    even_list = [0, 2, 4, 6, 8]
    last_char = str(number)[-1]
    return int(last_char) in even_list

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')



"""
Или же можно воспользоваться бинарной опцией:
def is_even(number:int) -> bool:
    return (number & 1) == 0
"""