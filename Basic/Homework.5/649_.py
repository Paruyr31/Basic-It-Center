n = input("input the text: ")
z1 = 0
z2 = -1

for i in range(len(n)):
    if n[i] == "z":
        z1 += i
        break

for i in range(z1 + 1, len(n)):
    if n[i] == "z":
        z2 += i
        break

count = z2 - z1 # count of simvols, from 'z' to 'z'

print(count)