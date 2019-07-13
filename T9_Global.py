# Global Scope
# for accessing we need not req [global l] decl

# l = 40 # global i.e gov. scheme(open to all)
# def Rahul(n):
#     global l# [global l] declaration should be before the use of 'l' if u are going to update global 'l'
#     # l = 10# local i.e personal
#     m = 20# local i.e personal
#     print(l,m)# here, first 'l' var will be checked in local scope-->if not found then it will go for global
#
#     l = l+20# it can only happen when "l" will be in local otherwise you can't update govt. sceme or
#     # (use [global l] declaration to update the global variable)
#     print(n,l)
#
# Rahul("hey i'm entered in Rahul() fn:")



def Rahul():
    x = 80
    def Rohan():
        global x # it will go directly, outside of the all fn() and update the global value if not exist it will create
        x = 90
    print("\nBefore caling rohan():",x)
    Rohan()
    print("After calling Rohan():",x)# here local will win
Rahul()
print(x)# 90 [updated value]



