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

for i in arr:
    if i == "f":
        arr2.append(i)
        arr2.append(i)
    else:
        arr2.append(i)

print(arr2)