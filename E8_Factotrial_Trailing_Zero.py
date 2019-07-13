# Part 1: cal the factorial
# Part 2: cal the no of trailing zeros in factorial

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)

    # # Iterative method
    # i = 1
    # fac = 1
    # for i in range (i,number+1,1):
    #     fac = fac *i
    # return fac


def factorialTrailingZeros(number):

    # 5! = 5*4*3*2*1
    count = 0
    # 100! = (100//5) + (100//5*5) jab tak zero na aa jaye
    i = 5
    while(number//i != 0):
        count += number//i
        i = i*5
    return count



    # fac = factorial(number)
    # print (fac)
    # count = 0
    # while (fac%10 == 0):
    #     count+=1
    #     fac = fac/10
    # return count



if __name__ == '__main__':
 try:
    number = int(input("enter the number:"))
    # fac = factorial(number)
    # print(f"Factorial of {number} is {fac}")

    facT = factorialTrailingZeros(number)
    print(f"\nNo Trailing Zeros in factorial:{facT}")
 except:
     print("plz enter the integer only")