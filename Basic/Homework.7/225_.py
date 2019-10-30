import math
n = int(input("list length = "))
t = int(input("t = "))
arg = 1
arr = []

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

for i in arr:
    if math.fabs(i) < t:
        arg *= i

print(arg)