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

result = math.pow(math.pow(x ** 2 + y ** 2, 5) + 4, 7) + math.sin(math.cos(x + y))

print(result)