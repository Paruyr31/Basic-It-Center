import math

x = int(input("x = "))

k = range(1, 5)

def calc(a):
    if x > 1:
        y = int(3*math.pow(x, a + 1))
        print("Y = "+str(y))
    else:
        y = int(5*x + math.pow(a, 7))
        print("Y = "+str(y))

for i in k:
    calc(i)