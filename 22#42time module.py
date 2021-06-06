import time

initial = time.time()

k = 0
while(k<45):
    print("this is Harry Bhai")
    k+=1
print("while loop ran in", time.time() - initial, "seconds")

initial2 = time.time()
for i in range(45):
    print("This is Harry Bhai")
print("for loop ran in", time.time() - initial2, "seconds")