import math

a = int(input("a = ")) # nermucum enq a
b = int(input("b = ")) # nermucum enq b
x = int(input("x = ")) # nermucum enq x

z = a*a+b*b

if z>5:
    y = 3*math.exp(a - x)+math.log((a*a+b*b+5), 3)
elif z<1:
    y = math.pow(math.tan(a + b), 4)
else:
    y = -3

print("Y = "+str(y))