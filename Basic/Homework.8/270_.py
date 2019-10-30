import math
import random

n = int(input("list length = "))
a = int(input("min = "))
b = int(input("max = "))
sqr_sum = 0
x = []
y = []

for i in range(n):
    x.append(random.randint(a, b))

print("X = "+str(x))

for i in range(n):
    y.append(random.randint(a, b))

print("Y = "+str(y))

for i in x:
    sqr_sum += math.pow(i, 2)

for i in y:
    sqr_sum += math.pow(i, 2)

print(sqr_sum)