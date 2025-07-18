lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
nonzeros = []
zeros = 0
for i in lst:
    if i != 0:
        nonzeros.append(i)
    else:
        zeros += 1

result = nonzeros + [0] * zeros
print(result)