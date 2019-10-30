import random

n = int(input("list length = "))
a = int(input("min = "))
b = int(input("max = "))
sum_x = 0
sum_y = 0
x = []
y = []

for i in range(n):
    x.append(random.randint(a, b))

print("X = "+str(x))

for i in range(n):
    y.append(random.randint(a, b))

print("Y = "+str(y))

for i in x:
    if i % 2 != 0:
        sum_x += i

for i in y:
    if i % 2 == 0:
        sum_y += i

print(sum_x - sum_y)