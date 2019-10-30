import math

x = float(input("x = "))
N = int(input("n = "))
result = x

for n in range(1, N+1):
    a = math.pow(x, 4*n + 1)/4*n + 1
    result += a

print(result)