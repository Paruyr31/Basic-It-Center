import math
n = int(input("list length = "))
k = int(input("k = "))
arr = []
m = 0

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

for i in arr:
    if int(i) % k == 0:
        m += math.pow(i, 2)

print(math.sqrt(m))