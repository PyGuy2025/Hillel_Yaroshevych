lst = [1, 3, 5]
paired_sum = 0
for i in lst:
    index = lst.index(i)
    if index == 0 or index % 2 == 0:
        paired_sum += i
result = paired_sum * lst[-1]
print(result)