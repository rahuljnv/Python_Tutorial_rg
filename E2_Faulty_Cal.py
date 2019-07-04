# Ex-2 Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

var1 = {"45*3":555, "55+9":77, "56/6":4}
var2 = ["+","-","*","/"]

while True:
  try:
    inch = int(input("Make ur choice:\n1.+ \n2.- \n3.* \n4./ \n5.Exit\n"))
  except:
      print("plz take input as integer only, w/o new line and white spaces")
      continue
  if inch > 5:
      print("plz choose from given set of operations")
      continue
  inp1 = input("Enter the 1'st No")
  inp2 = input("Enter the 2'nd NO")


  if inch == 5:
      exit()
  try:
   if inch == 1:
      if (inp1+var2[0]+inp2) in var1.keys():
          print(var1.get((inp1+var2[0]+inp2)))
      else:
         print(int(inp1) + int(inp2))
   elif inch == 3:
      if (inp1+var2[2]+inp2) in var1.keys():
          print(var1.get((inp1+var2[2]+inp2)))
      else:
          print(int(inp1) * int(inp2))
   elif inch == 4:
       if (inp1+var2[3]+inp2) in var1.keys():
          print(var1.get((inp1+var2[3]+inp2)))
       else:
          print(int(inp1) / int(inp2))

   else:
        print(int(inp1) - int(inp2))
  except:
       print("plz take input as integer only, w/o new line and white spaces")
