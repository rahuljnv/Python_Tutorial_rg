# E7- write a python program to generate kirana Bill

sum = 0
while True:
    userInput = input("Enter the price or press 'q' to quit\n")
    try:
       if userInput != 'q':
          sum = sum + int(userInput)
          print(f"your Amount so for:{sum}")

       elif userInput == 'q':
           print(f"Your Total amount is:{sum}\nThank you for shopping with US, Have a great day!!!")
           break
    except:
        print("plz input integer only")
        continue
