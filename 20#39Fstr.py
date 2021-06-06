#F function

import math
me = "Sandy"
a1 = 3
a = "This is a % s" % me
print(a,a1)

a = "This is {1} {0}"
b = a.format(me,a1)
print(b)

a = f"This is {me} {a1} {math.cos(90)}"
print(a)