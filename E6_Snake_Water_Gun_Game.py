# Ex-6 Snake water gun
# Create a snake water gun game in Python! Search Snake water gun game in google if you need help on rules and how to play the game!
# snake-snake -- tie
# snake-water -- snake(snake will drink water)
# snake-gun -- gun(snake will die)
# water-gun -- water(gun will sink)


import random

lst = ["snake","water","gun"]
cpu_p = 0
user_p = 0
try:
 no_atmpt = int(input("Enter your no of Attempts\t"))
except:
    print("plz input integer only")
    exit()


def snake(snake, r_n):
    global user_p, cpu_p
    if snake == r_n:
        # pass
        print("tie")
    elif snake != r_n:
        if r_n == "water":# (water, snkae)--user
            user_p += 1
        else:# (gun, snake)--cpu
            cpu_p += 1


def water(water, r_n):
    global user_p, cpu_p
    if water == r_n:
        # pass
        print("tie")
    elif water != r_n:
        if r_n == "snake":# (snake, water)--cpu
            cpu_p += 1
        else:# (gun, water)--user
            user_p += 1

def gun(gun, r_n):
    global user_p, cpu_p
    if gun == r_n:
        # pass
        print("tie")
    elif gun != r_n:
        if r_n == "snake":# (snake, gun)--user
            user_p += 1
        else:# (water, gun)--cpu
            cpu_p += 1

while no_atmpt > 0:
    ch = input("What do you want to take\t's':snake 'w':water 'g':gun\n")
    ch.lower()
    r_n = random.choices(lst)
    r_n = r_n[0] # converting from list to str
    # print(r_n)
    # print(type(r_n))
    if ch == 's' or ch == "S":
        snake("snake", r_n)
    elif ch == "w" or ch == 'W':
        water("water", r_n)
    elif ch == "g" or ch == "G":
        gun("gun", r_n)
    else:
        print("plz choose the given input only")
        continue
    no_atmpt -= 1



for i in range(1, 10, 5):
    print(10*"*")

print(f"you'r score is {user_p}")
print(f"Computer score is {cpu_p}")

if user_p > cpu_p:
    print(f"you won!!, Enjoy the glory")
elif user_p < cpu_p:
    print(f"Oooo sorry, Computer won")

else:
    print("WOW!! Match Tied")
