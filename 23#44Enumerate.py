Sandy = ["Aloo", "BHindi", "Lolipop", "chawmin"]


i = 1
for item in Sandy:
    if i%3 != 0:
        print(f"Jarvis please buy {item}")
    i += 1


for index, item in enumerate(Sandy):
    if index%2==0:
        print(f"Jarvis please buy {item}")