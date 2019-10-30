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

while True:
    q = input("please input: 'up' or 'on here'? ")
    if q == "up" or q == "on here":
        break
    else:
        print("wrong answer!")

k = int(input("k = "))

prod = 1

if q == "up":
    for i in range(m - 1):
        for j in range(m - i - 1):
            if arr[i][j] % k == 0:
                prod *= arr[i][j]
else:
    for i in range(m):
        for j in range(m):
            if i + j == m - 1:
                if arr[i][j] % k == 0:
                    prod *= arr[i][j]

print()
print(prod)