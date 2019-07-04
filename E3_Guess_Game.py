# Ex-3 SMART_GUESS_GAME
# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over
while True:
 try:
    n = int(input("Set reference number want to make guess\t"))
    no_guess = int(input("How many attempts u want\t"))
 except:
    print("plz give input as integer only w/o new line and white spaces")
    continue
 if True:
     break

print("Hey welcome to the Smart Guess!")
print("Choose your Number:\t")

rmc = no_guess
while(True):

    if(rmc == 0):
        print("Sorry!! Better Luck Next Time!!!")
        break
    else:
        rmc -= 1
        try:
           inp = int(input())
        except:
            print("plz give input as integer only w/o new line and white spaces")
            rmc += 1
            continue
            # exit()

        if(inp == n):
            print("Congrats!! you are winner, Enjoy the Glory\nNo of Guesses are left:", rmc)
            break
        elif(inp < n):
               print("Your no. is Smaller,\nNo of Guesses are left:", rmc)

        else:
            print("Your no. is Bigger,\nNo of Guesses are left:", rmc)

        if rmc != 0:
           print("try, again:\t")



