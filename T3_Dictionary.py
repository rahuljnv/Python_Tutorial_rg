# Dictionary is key-value pairs

d1 = {}
# print(type(d1))
d2 = {"John":"Burger", "Rohan":"Fish","Skillf":"Roti",
      "Shubham":{"B":"Maggie","L":"Roti","D":"Chicken"}}
print(d2)# whole dict
print(d2["Rohan"])
print(type(d2["Rohan"]))# <class 'str'>
print(d2["Shubham"])
print(type(d2["Shubham"]))# <class 'dict'>

print((d2["Shubham"]["B"]))# returns Maggie
print(type(d2["Shubham"]["B"]))

# """
# so in dict VALUE of the key can be-
# dict or tuple or list
#
# keys are IMMUTABLE
# """

# Dict modification
d2["Arun"] = "Junk food"# added at last
d2[420] = "KAbab"
print(d2)
del d2[420]
print(d2)

# # dict copy--NOT GOOOD APPROACH
# d3 = d2# here d3 works as pointer so, changes will reflect on both
# del d3["John"]
# print("hey",d2,"\n",d3)

# # dict copy--Good Approach
# d3 = d2.copy()
# del d3["Rohan"]
# print(d2)


d2.update({"Leena":"Toffe"})# at last
print("Updated dict",d2)

print(d2.get("Ravi"))# return None(if key not exist)
#print(d2["Ravi"])# error, "Ravi" isn't exist
print(d2.keys())
print(d2.items())



