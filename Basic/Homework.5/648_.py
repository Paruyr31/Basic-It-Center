n = input("input the text: ")
count = 0 # count of '0'

for i in range(len(n)):
    if n[i] == "x":
        x = i
        break

while x <= len(n) - 1:
    if n[x] == "0":
        count += 1
    x += 1

print(count)