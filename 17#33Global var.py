l = 50 #global
def function1(n):
    l = 5 #local
    m = 8
    #global l
    l = l + 5
    print(l,m)
    print(n, "i have printed")

x =89
def harry1():
    x = 20
    def rohan():
        global x
        x = 88
    rohan()
    print("calling to rohan()", x)


harry1()
print(x)
