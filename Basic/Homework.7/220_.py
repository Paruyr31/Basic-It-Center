n = int(input("list length = "))
count_pos = 0 # count of positive numbers
count_neg = 0 # count of negative numbers
arr = []

for i in range(n):
    arr.append(int(input("arr["+str(i)+"] = ")))

for i in arr:
    if i >= 0:
        count_pos += 1
    else:
        count_neg += 1

print(str(count_pos)+" positive number and "+str(count_neg)+" negative")