a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
max = a

arr = [a, b, c]

for i in arr:
    if i > max:
        max = i

print("Max = "+str(max))