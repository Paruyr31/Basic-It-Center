n = int(input("list length = "))
arr = []

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

max = arr[0]
for i in arr:
    if i > max:
        max = i

print("max = "+str(max))