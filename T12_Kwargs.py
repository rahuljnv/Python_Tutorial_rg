# Args & Kwargs [Order is imp]

def Rahul(normal, *argsrahul, **kwargsrahul):
    print(type(argsrahul))# tuple
    print(type(kwargsrahul))# dict
    print(f"These are {normal}")

    for item in argsrahul:
        print(item)
    for key, value in kwargsrahul.items():
        print(f"{key} is {value}")


normal = "my friends"
har = ["karry","jarvis","tiger","rishi","kshitiz"]
kw = {"rahul":"Programmer","Abhi":"Actor"}

Rahul(normal, *har, **kw)

