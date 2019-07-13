# Lambda functions or anonymous functions-> lambda fn is one liner fn.

# def add(a, b):
#     return a+b
#
# minus = lambda x, y: x-y
# def minus(x, y):
#     return x-y
#
# print(minus(9, 4))
# precedence depends which one is more recent[if we defined both lambda minus & normal fn]



# a =[[1, 14], [5, 6], [8,23]]
# a.sort(key = lambda x:x[1])
# print(a)
#
# def a_first(a):
#     return a[1]
# a.sort(key = a_first)
# print(a)

# Map
# map()--return map object
# if u want to apply some fn into whole iterable.
num = [1,2,3,34,4,5,23]
print(list(map(lambda n: n + 2, num)))
print(num)

# Filter
# filter()--return filter object
# is used to filer the things we need from iterable--if return true
print(list(filter(lambda n: n % 2 != 0, num)))
print(num)

# Reduce
# is used to reduce into a single entity from iterable
from functools import reduce
print(reduce(lambda x, y: x + y,num))
print(num)