a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

arr = [a, b, c]

d = arr[1] - arr[0]

if b + d == c:
    print("true")
else:
    print("false")