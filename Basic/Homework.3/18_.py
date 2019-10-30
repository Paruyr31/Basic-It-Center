import math

x = int(input("x = "))
z = int(input("z = "))

if 1 <= x and x <= 7:
    y = math.pow(math.fabs(x) + 2*math.fabs(z), 1/4) + math.exp(math.fabs(x + 1))
else:
    y = math.pow(math.tan(math.pow(x + z, 7)), 2)
print("Y = "+str(y))