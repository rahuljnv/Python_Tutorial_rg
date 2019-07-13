# # Lists and Lists Function
#
# num = [1,234,34,221,678]
# grocerry = ["Bhindi","Harpic","Mango","Capsicum","Toothpaste"]
# string = (max(grocerry))# returns string with max length(i.e Toothpaste)
# # Note: when u apply max() always check whether container has same data types as whole
# print(len(string))
# print(len(max(grocerry)))
# print(len(grocerry))# length of grocerry
# print(max(num))# 678 is max
# print(len(grocerry[4]))
# print(grocerry)# print the whole list
#
# grocerry.sort()# here alpha sort & MAKE CHANGES TO THE ORIGINAL LIST(error: in case of multiple data types)
# print(grocerry)# after sorting the list
# grocerry.reverse()# reversal of list & TRANSLATE THE CHANGES TO THE ORIGINAL
# print(grocerry)

# # slicing returns sliced list BUT Original does not change
# numbers = [2,3,5,1,6]
# print(numbers[::2])
# print(numbers)# It won't change original
# print(numbers[::-1])# It will reverse
# print(numbers[::-2])
#
# # IMP POINTS
# print(numbers[1:5:-2])# don't go -2,-3 so on
# print(numbers[1:5:-1])
#
# # Functions
# numbers.append(89)# append at last
# numbers.append(56)
# print(numbers)
# numbers.insert(2,55)# insert at index = 2
# print(numbers)
# #numbers.remove(68)# error 68 is not in the list
# numbers.remove(6)
# print(numbers)
# numbers.pop()# last element will be pop-out
# print(numbers)

# # Tuple
# numbers = [2,3,5,1,6]
# numbers[1] = 98# mutable
# print(numbers)
#
# tp = (1,2,3)
# #tp[1] = 56 Immutable
# print(tp)
#
# # swapping
# a = 23
# b = 45
# print(a,b)
# a,b = b,a
# print(a,b)





