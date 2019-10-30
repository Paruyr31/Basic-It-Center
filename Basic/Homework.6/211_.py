lines = int(input("line count: "))
y = 1  # count of '*'
z = lines - 1  # count of 'space'
a = "* "
b = " "

while y <= lines:
    print(z * b + y * a)
    z -= 1
    y += 1