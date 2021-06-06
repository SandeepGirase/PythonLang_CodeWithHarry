print("WELCOME TO THE HEALTH MANAGEMENT SYSTEM")
print("choose ur choice to get data")
print("1.for HARRY,2.for ROHAN,3.for HAMMAD")
print("A.for DIET,B.for GYM SCHEDULE")
f=0
def getdate(x,f):
    for line in f:
        t = line.find(x)
        print(line[t:])


def getdata(a,b):
    if a=='1'and b=='A':
        f = open("harrydiet,py")
        print(f.readline())
        getdate(x,f)
    elif a=='1'and b=='B':
        f = open("harrygym.py")
        print(f.readline())
        getdate(x,f)
    elif a == '2' and b == 'A':
        f = open("rohandiet.py")
        print(f.readline())
        getdate(x,f)
    elif a == '2' and b == 'B':
        f = open("rohangym.py")
        print(f.readline())
        getdate(x,f)
    elif a == '3' and b == 'A':
        f = open("hammaddiet.p")
        print(f.readline())
        getdate(x,f)
    elif a == '3' and b == 'B':
        f = open("hammadgym.py")
        print(f.readline())
        getdate(x,f)
print("Enter ur choices")
a=input("enter choice for candidate")
b=input("enter choice for details")
print("Enter the time at which u want to access the data")
x =str(input("enter the time"))
getdata(a,b)