a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

arr = [a, b, c]

q = arr[1]/arr[0]

if b*q == c:
    print("true")
else:
    print("false")