x = int(input("x = ")) # nermucum enq x
y = int(input("y = ")) # nermucum enq y

a = x*x+y*y

if y>=0:
    if a>=1 and a<=4:
        z = 0
    else:
        z = x + y
    print("z = "+str(z))
else:
    print("nermucel 'y'-i drakan arjeq")