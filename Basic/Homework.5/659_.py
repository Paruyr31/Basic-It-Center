n = input("input the text: ")

c = 0 # count of 'c'
d = 0 # count of 'd'

if "x" in n:
    for i in n:
        if i == "c":
            c += 1
    print("count of 'c' = "+str(c))
else:
    for i in n:
        if i == "d":
            d += 1
    print("count of 'd' = "+str(d))