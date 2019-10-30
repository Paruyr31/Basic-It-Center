import random

def array(n, min, max):
    for i in range(n):
        arr.append(random.randint(min, max))
    return arr

n = int(input("n = "))
min = int(input("min = "))
max = int(input("max = "))
arg = 1
arr = []
arr_2d = []

for i in range(n):
    arr = array(n, min, max)
    arr_2d.append(arr)
    arr = []

print("arr_2d = "+str(arr_2d))

for arr in arr_2d:
    for a in arr:
        arg *= a

print(arg)