a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

n = 0 # zuyg tveri qanaky

arr = [a, b, c]

for i in arr:
    if i % 2 == 0:
        n += 1

if n != 0:
    print("1")
else:
    print("2")