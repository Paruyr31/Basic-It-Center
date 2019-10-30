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
    q = input("please input: 'down' or 'on here'? ")
    if q == "down" or q == "on here":
        break
    else:
        print("wrong answer!")

sum = 0
count = 0

if q == "down":
    for i in range(1, m):
        for j in range(i):
            if arr[i][j] % 2 == 0:
                sum += arr[i][j]
                count += 1
else:
    for i in range(m):
        for j in range(m):
            if i == j:
                if arr[i][j] % 2 == 0:
                    sum += arr[i][j]
                    count += 1

print()
print(sum/count)
