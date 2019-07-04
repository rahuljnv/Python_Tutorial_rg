# Ex-4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *

while True:
    try:
       n = int(input("Enter the no. of rows, want to print:\t"))
       choice = int(input("Enter your choice:\t1.True or 0.False"))
    except:
       print("plz take input as integer only, avoid n\w and white spaces")
       continue
    if True:
        break
# if choice > 1 or choice < 0:
#     print("plz take input 1 or O")
#     exit()

if choice == 1:
    for i in range(1, n+1, 1):
        print(i*"*", end = "\n")

elif choice == 0:
    while(n > 0):
        print(n*"*", end = "\n")
        n -= 1;


else:
   print("plz choose the given choices only")


