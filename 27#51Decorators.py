def function1():
    print("Subcribe now")
fun2 = function1
del function1
fun2()
