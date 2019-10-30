import math

def input_x():
    while True:
        try:
            x = int(input("x = "))
            return x
        except ValueError:
            print("nermucel tiv")
            continue

def input_y():
    while True:
        try:
            y = int(input("y = "))
            return y
        except ValueError:
            print("nermucel tiv")
            continue

x = input_x()
y = input_y()

result = (math.pow(2, x) - 5)/(math.pow(3, y) + 2) + math.log((math.fabs(x) + 1) + math.pow(y, 2))

print(result)