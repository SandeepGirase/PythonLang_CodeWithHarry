#dictionary is nothing but key value pairs
d1 = {}
print(type(d1))
d2 = {"Sandeep":"burger","rohan":"fish","skillf":"roti"}
print(d2["rohan"])
d2 ["ankit"] = "chicken"
del d2["skillf"]
d2.update({"leena":"mamidian"})
print(d2.keys())
print(d2.items())