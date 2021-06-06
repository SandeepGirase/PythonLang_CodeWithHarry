#def function_name_print(a,b,c,d,e):
 #   print(a,b,c,d,e)


def funargs(normal, *argsrohan):
    print(normal)
    for item in argsrohan:
        print(item)
#function_name_print("Harry","Rohan", "Skillf", "Hammad", "Sandy")
har = ("Harry", "Rohan", "Skillf", "Hammad", "Sandy", "i am programmer")
normal = "i m a normal argumet and the student are :"
funargs(normal, *har)