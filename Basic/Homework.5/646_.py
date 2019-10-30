n = input("input the text: ")
a = 0 # count of 'a'

for i in range(len(n)):
    if n[i] == "a":
        a += 1

print(a)