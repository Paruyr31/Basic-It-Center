n = int(input("list length = "))
sum = 0
arg = 1
arr = []

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

for i in arr:
    if i % 2 == 0:
        sum += i
        arg *= i

print("sum = "+str(sum))
print("arg = "+str(arg))