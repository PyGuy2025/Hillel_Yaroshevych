lst = [12, 3, 4, 10, 8]
if len(lst) <= 1:
    print(lst)
else:
    lst.insert(0, lst.pop())
    print(lst)