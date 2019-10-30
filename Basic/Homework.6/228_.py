n = int(input("list length = "))
k = int(input("k = "))
sum = 0
arr = []

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

for i in range(len(arr)):
    if i % k == 0:
        sum += arr[i]

print(sum)