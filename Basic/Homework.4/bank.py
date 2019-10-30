n = 0 # hertum spasoxneri tivy

print("0 - Durs gal bankic")
print("1 - Amragrel hert")
print("2 - Hertum mardkanc qanaky")
print("3 - Chexarkel herty")

def input_number(message):
    while True:
        try:
            i = int(input(message))
            if i >= 0:
                return i
        except ValueError:
            print("nermucel tiv")
            continue

while True:

    i = input_number(">> ")

    if i == 0:
        break
    elif i == 1:
        """amragrel hert"""
        n += 1
    elif i == 2:
        """hertum mardkanc qanaky"""
        print("hertum spasum e "+str(n)+" hogi")
    elif i == 3:
        """chexarkel herty"""
        n -= 1