n = list(input("input the text: "))

i = 0

while i <= len(n):
    n[i] = "a"
    i += 3

a = ''.join(n)

print(a)