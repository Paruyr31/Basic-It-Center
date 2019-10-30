import math

x = int(input("x = ")) # nermucum enq x
y = int(input("y = ")) # nermucum enq y

a = math.fabs(x*x - y)/x*x + y*y # ctg-i meji artahaytutyunn arandzin

p = math.cos(a)/math.sin(a) + math.log((x*x + 1), 10) # hashvum enq artahaytutyan arjeqy ev talis "p" popoxakanin

print("Patasxan: "+str(p)) # tpum enq patasxany