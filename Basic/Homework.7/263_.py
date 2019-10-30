n = int(input("list length = "))
count = 0 # count of positive numbers
x = []
y = []

for i in range(n):
    x.append(int(input("X["+str(i)+"] = ")))

for i in range(n):
    y.append(int(input("Y["+str(i)+"] = ")))

for i in x:
    if i > 0:
        count += 1

for i in y:
    if i > 0:
        count += 1

print(count)