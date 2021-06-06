#def print2(str1):
#    print2(str1)
#    print("This is"+ str1)
#

#print2("Harry")



def factorial(n):
    """
    :param n: Integer
    :return: n * n-1 * n-2 * n-3.........1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

number = int(input("Enter your number: "))
print("Factorial using interative method", factorial(number))