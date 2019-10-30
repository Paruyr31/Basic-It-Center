import random

n = int(input("n = "))

arr = []

for l in range(n):
    arr.append([])

print("please input minimum and maximum values in matrix")
x = int(input("min = "))
y = int(input("max = "))

for i in range(len(arr)):
    for j in range(n):
        arr[i].append(random.randint(x, y))

print()
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end="  ")
    print()
print()

"""start program"""

print("[a; b]")
a = int(input("a = "))
b = int(input("b = "))

count = 0

for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[i][j] >= a and arr[i][j] <= b:
            count += 1

print()
print(count)