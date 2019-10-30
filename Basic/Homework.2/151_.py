import math

x = int(input("x = "))  # nermucum enq x
n = int(input("n = "))  # nermucum enq n
i = 1
s = 0


def faktorial(tiv):  # faktorial hashvelu funkcia
    f = 1
    for i in range(1, tiv + 1):
        f *= i
    return f


while i <= n:
    s += (math.pow(math.log(3, math.e), i) / faktorial(i)) * math.pow(x, i)
    i += 1

print("S = " + str(s))