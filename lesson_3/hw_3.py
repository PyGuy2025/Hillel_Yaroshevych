lst = [1, 2, 3, 4, 5, 6, 7, 8]
length = len(lst)
if length == 0:
    result = [[], []]
else:
    mid = (length + 1) // 2
    result = [lst[:mid], lst[mid:]]

print(result)