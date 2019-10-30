n = int(input("list length = "))
count = 0
arr = []

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

for i in arr:
    if i is 0:
        count += 1

print(count)