import math

x = int(input("x = "))

k = range(2, 8) # range(2, 9, 1) = range(2, 9)

def calc(a):
    if x < 6:
        y = int(math.pow(x, a) + a)
        print("Y = "+str(y))
    else:
        y = int(math.log(a, 5))
        print("Y = "+str(y))

for i in k:
    calc(i)