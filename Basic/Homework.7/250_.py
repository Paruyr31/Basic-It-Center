import math
n = int(input("list length = "))
arg = 1
arr = []

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

for i in range(len(arr)):
    if (arr[i]*i) % 3 == 2:
        arg *= math.pow(arr[i], 2)

print(int(arg))