import math

x = int(input("x = "))

k = range(2, 9) # range(2, 9, 1) = range(2, 9)

def calc(a):
    if 3 < x and x < 7:
        y = int(9*math.pow(x, a))
        print("Y = "+str(y))
    else:
        y = int(8*x + math.pow(a, 3))
        print("Y = "+str(y))

for i in k:
    calc(i)