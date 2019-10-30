n = int(input("list length = "))
sum = 0
count = 0
arr = []

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

for i in arr:
    if i % 2 != 0:
        sum += i
        count += 1

print(sum/count)