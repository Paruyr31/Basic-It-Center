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

while True:
    q = input("please input: 'down' or 'on here'? ")
    if q == "down" or q == "on here":
        break
    else:
        print("wrong answer!")

count = 0

if q == "down":
    for i in range(1, n):
        for j in range(n - i, n):
            if (i + j) % 2 != 0:
                count += 1
else:
    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                if (i + j) % 2 != 0:
                    count += 1

print()
print(count)