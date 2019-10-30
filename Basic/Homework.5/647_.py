n = input("input the text: ")
n_reverse = ""
i = len(n) - 1

while i >= 0:
    n_reverse += n[i]
    i -= 1

if n == n_reverse:
    t = True
else:
    t = False

print(t)