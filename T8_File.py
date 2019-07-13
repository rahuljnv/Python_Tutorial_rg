# File Io Basics
"""
"r" - Open file for reading - default(it won't create file if not exist
"w" - Open a file for writing--(it wil create if file doesn't exist)
"x" - Creates file if not exists
"a" - Add more content to a file
"t" - text mode - default
"b" - binary mode
"+" - read and write
"""

# 1.read
#
# f = open("rg.txt")
# content = f.read()
# print((content))
#
# f = open("rg.txt","rb")# rb mode-binary mode
# content = f.read()
# print(content)
#
# f = open("rg.txt","rt")# rt-default mode
# content = f.read()
# print(content)
#
# f = open("rg.txt","rt")
# content = f.read(3)# read only 3 char
# print(content)
# content = f.read(3)# read next 3 char
# print(content)
#
#
# f = open("rg.txt","rt")
# content = f.read(333333)
# print("1ong enough", content)
#
# content = f.read(34455)# No more char remain--nothing will print
# print("\nHey file is already read completely",content)
#
#
# f = open("rg.txt","rt")
# content = f.read()
# for line in content:# char by char iteration will happen
#      print(line)
#
# f = open("rg.txt","rt")
# for line in f:
#     print(line, end="")# By default new line will be printed Not coz of print.
#
#
# f = open("rg.txt","rt")# n/w line will be printed
# print(f.readline())
# print(f.readline())
#
#
# f = open("rg.txt")
# print(f.readlines())
# f.close()

# 2.write and append

# f->file handler
# f = open("rg2.txt","w")# it will clear and write the content every time
# c = f.write("Hey i'm rg2, T8 tut")
# print(c)# 19(i.e no of char written)
# f.close()


# f = open("rg2.txt","a")# it will append w/o clearing the prev content
# c = f.write("\nhey dude its the append mode\n")
# print(c)# total char written is 30 including 2(\n) + current appended content
# f.close()


# # Handle read and write both
#
# f = open("rg2.txt","r+")
# print(f.read())
# c = f.write("\nThank you brother..!!i\n")
# print(c)
# f.close()

# # L3- seek and tell

# f = open("rg.txt")
# print(f.tell())# will tell the file pointer or file handler position
# print(f.readline())
# print(f.tell())
# print(f.readline())
# f.seek(5)# keep file handler at char '5'
# print(f.tell())
# f.close()

# L4-File open 'with'
#
# with open("rg.txt") as f:
#     a = f.readlines()
#     print(a)

# f = open("rg.txt","rt")
# a = f.read()
# print(a)
# f.close()