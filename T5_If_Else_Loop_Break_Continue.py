# L1
# IF Else ladder

# var1 = 6
# var2 = 45
# var3 = int(input())

# NOT efficient if "if" cond'n will get true then, it will check all if
# if var3 > var2:
#     print("Greater")
#
# if var3 == var2:
#     print("Equal")
#
# else:
#     print("Smaller")


# # here, if 'if' will get true then, will execute the block and come out from ladder
# if var3 > var2:
#     print("Greater")
#
#
# elif var3 == var2:
#     print("equal")
#
# else:
#     print("Smaller")
#
#
# lis = [1,2,3,4,5]
# print(5 in lis)# True
# if 15 not in lis:
#     print("15 is not in the list")


# L2-Loop
# For loop- when you know the no. of iteration

# list1 = ["Karry","Larry","Marry","Carry"]
# for item in list1:
#     print(item)

# list2 = [["Karry",1], ["Larry",34], ["Marry",30], ["Carry",89]]
# for item in list2:
#     print(item)
#
# for i in range(len(list2)):
#     print(list2[i])
#
# for item, loolypop in list2:
#     print(item, "and Lollypop is", loolypop)
#
# dict1 = dict(list2)
# print(dict1)
# """
# HERE Unpacking don't work
# # for item, loolypop in dict1:
# #     print(item, "and Lollypop is", loolypop)
#
# """
# for item,loolypop in dict1.items():
#     print(item, "and Lollypop is", loolypop)
#
# # only key you will get
# for item in dict1:
#     print(item)
#
# items = [int, float, "carry", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]
# for item in items:
#     if str(item).isnumeric() and item <= 6:
#         print(item)
# print("4".isnumeric())# True
#
#
# # while loop--when u don't know the exact limit
# i = 0
# while(i < 4):
#     print(i)
#     i = i + 1


# L3-Break and continue

# i =0
# while(True):
#     if i+1 < 5:
#         i = i + 1
#         continue
#     print(i+1, end=" ")
#     if(i == 44):
#         break # come out from the loop
#     i = i + 1
#

# while(True):
#     inp = int(input("Enter a Number\n"))
#     if inp > 100:
#         print("you have entered a number greater than 100\n")
#         break
#     else:
#         print("Try again!\n")
#         continue