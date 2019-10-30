n = int(input("list length = "))
count = 0
sum = 0
arr = []

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

for i in arr:
    if i < 0:
        sum += i
        count += 1

print(sum/count)