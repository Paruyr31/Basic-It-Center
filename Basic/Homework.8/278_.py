n = int(input("list length = "))
arr = []
arr2 = []
round = 0

while True:
    inp = input("X["+str(round)+"] = ")
    if len(inp) == 1:
        arr.append(inp)
        round += 1
    if round == n:
        break

for i in range(len(arr)):
    if i % 2 == 0:
        arr2.append(arr[i])

print(arr2)