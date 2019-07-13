
# # L1
# # single line comment
#
# """multi
# line comment"""
#
# # escape sequence
# print("c:\narry")
# print("c:\\narry")
# print("C\"narry\"")
#
# print("rishi is good boy","rohan is not")# by default n/w line get added
#
# print("jai is good boy",",","but rohan is not", end=", ")# here "," will be added at end of string
#
# print("jai is not good boy1", end=" HOPE" " rohan is not2 ")
#
# print("jay is good boy", end=" 89 ")
#
# print("jai is good boy","rohan is not")
#
# print("this is new line \nAnd this is next blank tab\t1")


# # L2
# # Variables and data types
#
# var1 = "hello"
# var2 = 4
# var3 = 67.4
# var4 = " rahul"
# print(type(var1))
# print(var1 + var4)# concatenation
# print(var2 + var3)# addition, result will be in float
# # print(var1 + var2)# error cancat is not possible
#
# var5 = "20 "
# var6 = "30"
# print(var5 + var6)# concatenation
# print(int(var5) + int(var6))# type casting
# print(5*int(var5)+int(var6))# 130
# print(5*str(int(var5)+int(var6)))# 5 times 50
#
# """
# str()
# int()
# float()
# """
#
# print(5 * "hello\n")
# intnum = input("your input will be taken as string always")
# print("new num is:", int(intnum)+20)
#
#
# # calculartor
#
# print("enter first num:")
# inp1 = input()
# print("enter second num:")
# inp2 = input()
# print("sum is:",int(inp1)+int(inp2))


# L3
# STRING Slicing & BUILT-IN FUNCTION

# mystr = "jai is a good boy"
# print(mystr[0:5])# [0,5)
# print(len(mystr))

# print(mystr[0:78])# till 78 but here whole string will be parsed, (len is < 78)
# # print(mystr[78])#error Index out of range
# print(mystr[0:5:2])
# print(mystr[::])# mystr[def = 0: def= len: def = 1]
# print(mystr[::666])# only first char here
#
# # negative slicing
# print(mystr[-4:-2])# start from [4th from last] then positive flow till last 2nd(excluding)
# print(mystr[::-1])# whole string will be reversed
# print(mystr[::-2])# string reversal with [-2] decr

# # Advanced
# print(mystr.isalnum())# False coz space is not alphanumeric
# print("tiger1".isalnum())# True [either numeric or alpha]
# print(mystr.isalpha())# False coz all char is not alphabet
# print(mystr.endswith("boy"))# True
# print(mystr.endswith("Boy"))# False
#
# # misc
# print(mystr.count("b"))# no. of 'b'
# print(mystr.count(" "))# no. of " "
# print(mystr.capitalize())# First letter will become capital
# print(mystr.find("is"))# return the index of first char(i.e 'i's)
# print(mystr.lower())# make lower case
# print(mystr.upper())# make upper case
# print(mystr.replace("is","are"))# replace "is" with "are"





