import math
n = int(input("list length = "))
k = int(input("k = "))
count = 0
arr = []

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

for i in range(len(arr)):
    if math.fabs(arr[i] - i) > k:
        count += 1

print(count)