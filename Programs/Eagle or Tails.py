import random
print("Throw a coin!!!")
eagle = 0
tails = 0
i = 0
while i != 100:
    a = random.randint(1, 2)
    i += 1
    if a == 1:
        eagle += 1
    elif a == 2:
        tails += 1

print("Eagle", eagle)
print("Tails", tails)



