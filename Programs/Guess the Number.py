import random
print("\tWelcome to the game 'Guess the Number!'")
print("\nI made a number from 1 -100")
print("Try to guess for the minimum number of attempts \n")
a = random.randint(1, 100)
b = int(input("Your number "))
count = 1
while b != a:
    if b > a:
        print("Less!")
    else:
        print("More!")
    b = int(input("Your number "))
    count += 1
print("Congrats!!! this number", a)
print("You needed", count, "attempts")
input('\n\nPress Enter. to leave')
