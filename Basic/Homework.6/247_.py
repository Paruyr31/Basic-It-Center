import math
n = int(input("list length = "))
m = 0
arr = []

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

for i in range(len(arr)):
    if arr[i] > i:
        m += math.pow(arr[i], 2)

print(math.sqrt(m))