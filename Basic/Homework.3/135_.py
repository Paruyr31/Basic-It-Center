import math

x = int(input("x = "))

k = range(1, 5)

def calc(a):
    if x > 1:
        y = int(math.pow(x, a - 1))
        print("Y = "+str(y))
    elif x < 3:
        y = int(x*math.pow(a, 3))
        print("Y = "+str(y))
    else:
        y = int(math.pow(10, -6))
        print("Y = "+str(y))

for i in k:
    calc(i)