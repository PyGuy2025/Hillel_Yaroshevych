def second_index(text:str, some_str:str) -> int or None:
    match_count = 0
    for elem in range(len(text) - len(some_str) + 1):
        if text[elem: elem + len(some_str)] == some_str:
            match_count += 1
            if match_count == 2:
                return elem
    return None

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')





