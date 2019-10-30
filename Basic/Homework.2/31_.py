a = int(input("a = ")) # nermucum enq a
b = int(input("b = ")) # nermucum enq b
c = int(input("c = ")) # nermucum enq c
d = int(input("d = ")) # nermucum enq d

max = a

if b>max:
    max = b
if c>max:
    max = c
if d>max:
    max = d

print("Max = "+str(max))