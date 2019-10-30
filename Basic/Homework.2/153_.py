import math

x = int(input("x = ")) # nermucum enq x
n = int(input("n = ")) # nermucum enq n

def faktorial(tiv): # faktoriali funkcia
    f = 1
    for i in range(1 ,tiv+1):
        f *= i
    return f

i = 1
s = 0

while i<=n:
    a = 2*i+1
    s += math.pow(x, a)/a
    i += 1

print("S = "+str(s))