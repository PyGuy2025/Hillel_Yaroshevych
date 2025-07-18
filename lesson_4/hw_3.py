import random as rnd

length = rnd.randint(3, 10)
lst = [rnd.randint(1, 10) for i in range(length)]
result = [lst[0], lst[2], lst[-2]]