n = int(input("list length = "))
arr = []
arr2 = []

for i in range(n):
    arr.append(int(input("X["+str(i)+"] = ")))

for i in arr:
    if i % 2 != 0:
        arr2.append(i)

print("Y = "+str(arr2))