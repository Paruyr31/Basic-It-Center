import math

x = -math.pi # skizb
end = math.pi # verj
step = math.pi/8 # qayl

while x <= end:
    y = math.pow(math.sin(x), 2) + math.cos(x)
    x += step
    print("Y["+str(x)+"] = "+str(y))