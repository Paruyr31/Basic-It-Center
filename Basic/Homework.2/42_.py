x = int(input("x = ")) # nermucum enq x
y = int(input("y = ")) # nermucum enq y

a = x/2+y/2
b = x*x+y*y

if y>=0 and x>=0: # stugum e te 'y'-y ev 'x'-y drakanen te voch
    if b>=1 and a<=1: # stugum e 'a'-i ev 'b'-i gtnvelu mijavayry
        z = x + y*y
    else:
        z = 5*x
    print("z = "+str(z)) # tpum e 'z'-y
else:
    print("nermucel 'y'-i ev 'x'-i drakan arjeq")