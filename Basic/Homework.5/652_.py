x = input("input the text: ")
y = input("input the text: ")

arr = []
string = ""

for i in y:
    count_x = 0 # count of 'i' in 'x'
    count_y = 0 # count of 'i' in 'y'
    if i in x:
        count_x += 1
    if i in y:
        count_y += 1
    if count_x != 0:
        arr.append(count_x)
        arr.append(count_y)
        count = min(arr)
        arr.clear()
        string += count*i
        x = x.replace(i, "")
        y = y.replace(i, "")

print(string)