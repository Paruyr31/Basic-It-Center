import math
n = int(input("list length = "))
m = 0
arr = []

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

for i in arr:
    if i < 0:
        m += math.pow(i, 2)

print(math.sqrt(m))