import math

a = int(input("a = ")) # nermucum enq a
x = int(input("x = ")) # nermucum enq x

if -5<=x and x<=5:
    y = math.pow((1 + a*a), 6)
elif x>5:
    y = math.cos(math.pow(math.log(math.fabs(x), math.e), 2)) + math.pow(x, 8)
else:
    y = a

print("Y = "+str(y))