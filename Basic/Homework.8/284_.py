n = int(input("list length = "))
arr = []

for i in range(n):
    arr.append(int(input("X[" + str(i) + "] = ")))

print("Y = [a; b]")
a = int(input("a = "))
b = int(input("b = ")) + 1

arr2 = arr[a:b]

print("Y = " + str(arr2))