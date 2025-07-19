lst = []
counter = 0
while 0 in lst:
    lst.remove(0)
    counter += 1
lst += [0] * counter
print(lst)