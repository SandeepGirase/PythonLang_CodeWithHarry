s = set() #Unique Keys
print(type(s))
s_from_list = set([1,2,3,4,5])
print(s_from_list)
print(type(s_from_list))
s.add(1)
s.add(2)
s1 = {4,6}
print(s.isdisjoint(s1))