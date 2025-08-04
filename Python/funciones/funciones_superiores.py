from functools import reduce


data = range(1,21)

# map()
map_gen = map(lambda x: x**2 / 2, data)
print(list(map_gen))

# filter()
filter_gen = filter(lambda x: x%2==1, data)
print(list(filter_gen))

# reduce()
sum_reduce = reduce(lambda a, b: a + b, data)
print(sum_reduce)