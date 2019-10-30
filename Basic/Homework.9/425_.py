import random

m = int(input("m = "))

arr = []

for l in range(m):
    arr.append([])

print("please input minimum and maximum values in matrix")
x = int(input("min = "))
y = int(input("max = "))

for i in range(len(arr)):
    for j in range(m):
        arr[i].append(random.randint(x, y))

print()
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end="  ")
    print()
print()

"""start program"""

count = 0

for i in range(1, m):
    for j in range(i):
        if arr[i][j] % 2 == 0:
            count += 1

print()
print(count)