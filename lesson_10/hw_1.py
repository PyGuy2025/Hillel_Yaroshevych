from inspect import isgenerator

def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    value = begin
    yield value
    for n in range(end-1):
        value = func(value)
        yield value

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')