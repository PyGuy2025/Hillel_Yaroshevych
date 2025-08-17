def difference(*args: int | float) -> int | float:
    n_list = set(args)
    if not n_list:
        return 0
    else:
        result = abs(max(n_list) - min(n_list))
        return round(result, 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')