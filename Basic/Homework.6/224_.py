import math
n = int(input("list length = "))
k = int(input("k = "))
sum = 0
arr = []

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

for i in arr:
    if math.fabs(i) < k:
        sum += math.pow(i, 3)

print(sum)