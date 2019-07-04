# Ex-1 Print the details of celebrity[say MSD]
# Using switch case

bio = {"Name":"MSD", "Lucky_No":7, "Hobby's":{"Bike collection", "playing cricket"}, "No of century's":50,
       "Want More_Info":"https://en.wikipedia.org/wiki/MS_Dhoni"}
# if you put exit() in dict then it will exit then n there at the time of dict execution


print("Enter the things want to know about MSD \n1.Name \n2.Lucky_No \n3.Hobby's \n4.No of century's \n5.Want More_Info \n6.Exit")
while True:
    try:
      u_inp = int(input())
    except:
        print("plz take input as integer only, avoid newline & white speces")
        continue
    switcher = {
    1:"Name",
    2:"Lucky_No",
    3:"Hobby's",
    4:"No of century's",
    5:"Want More_Info",
    6:"Exit"
     }
    if u_inp == 6:
       exit()
    if u_inp > 6:
        print("plz choose in the given choices")
        continue
    print(bio.get(switcher.get(u_inp, "nothing")))

