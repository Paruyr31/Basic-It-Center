import math

a = int(input("a = "))
b = int(input("b = "))
x = int(input("x = "))

p = a + math.fabs(b) # payman
if p < -5:
    y = math.exp(math.fabs(a + x))*math.pow(math.cos(a + x + b), 2)
elif p > 2:
    y = math.pow(math.atan(a + x), 1/3)
else:
    y = p
print("Y = "+str(y))