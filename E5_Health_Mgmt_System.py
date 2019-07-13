# E-5 Health Management System
# 3 clients - Deepu, Kshitiz and Rishabh

# Total 6 files(initial clients)
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any clients

def getdate():
    import datetime
    return (datetime.datetime.now())

def registerClient(client):
    reg_date = str(getdate())
    client_f = client + '_f'
    with open(f"{client_f}.txt", "a") as f:
        f.write("Registration date\t" + reg_date)
    client_e = client + '_e'
    with open(f"{client_e}.txt", "a") as f:
        f.write("Registration date\t" + reg_date)

def addContent(client, content, ch):

    content_added_at_time = str(getdate())
    if ch == 1:
        client_e = client + '_e'
        with open(f"{client_e}.txt", "a") as f:
            f.write("\n" + content + "\t" + content_added_at_time)
    elif ch == 2:
        client_f = client + '_f'
        with open(f"{client_f}.txt", "a") as f:
            f.write("\n" + content + "\t" + content_added_at_time)
    else:
        print("you have chosen wrong option")


def retrieveExeFood(client, choice):
    if choice == 2:# Exercise
        name1 = client + "_e"
        f = open(f"{name1}.txt", "r")
        content = f.read()
        print(content)
        f.close()
    else:# food
        name2 = client + "_f"
        with open(f"{name2}.txt","r") as f:
            content = f.readlines()
            print(content)

if __name__ == '__main__':
    clients = ["deepu","rishabh","kshitiz"]
    for client in clients:
        registerClient(client)
    client = input(("Enter the client name\t"))
    choice = int(input(
        "\nWhat would you like to know sir\n1.preferred food\n2.preferred exercise\n3.add or modify existing log"))

    if client in clients:
        print("Catching ur request sir...")
        if choice == 1 or choice == 2:
            retrieveExeFood(client, choice)
        elif choice == 3:
            print("which log, would you like to modify 1.exercise log 2.food log")
            ch = int(input())
            addContent(client, input("plz write here..."), ch)
        else:
            print("Invalid option")
    else:
        print(
            "\nIt seems you are not our registered clients\nwould you like to register\n1.register\n2.Not willing to register")
        register = int(input())
        if register == 1:
            print("\nprocessing ur request...")
            clients.append(input("Enter your name"))
            print(clients)
            registerClient(clients[len(clients) - 1])
            print("\nCongrats you are done with registration, Happy membership..!")
        elif register == 2:
            print("\nThank you for coming sir, have a good day..!")
        else:
            print("\nPlz, check ur option")



