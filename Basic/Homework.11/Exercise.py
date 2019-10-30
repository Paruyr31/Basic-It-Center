def sum(n):
    if n == 0:
        return n
    return n + sum(n-1)

#####################
##   EXERCISE 2    ##
#####################
def pr(string):
    if len(string) == 0:
        return
    print(string[0])
    pr(string[1:])

#####################
##   EXERCISE 3    ##
#####################
def prod(filename):
    f = open(filename)
    first_line = f.readline()
    second_line = f.readline()
    f.close()
    f_line = first_line.split(",")
    s_line = second_line.split(",")
    fl = []
    sl = []
    for i in f_line:
        fl.append(int(i))
    for i in s_line:
        sl.append(int(i))
    f_max = max(fl)
    s_min = min(sl)
    return f_max*s_min

#####################
##   EXERCISE 4    ##
#####################
def item_count(filename):
    count = 0
    f = open(filename)
    f_line = f.readline()
    s_line = f.readline()
    t_line = f.readline()
    f.close()
    for i in f_line:
        if i == "a":
            count += 1
    for i in s_line:
        if i == "z":
            count += 1
    for i in t_line:
        try:
            i = int(i)
            count += 1
        except ValueError:
            continue
    return count

#####################
##   EXERCISE 5    ##
#####################
def sum_arr(filename, arr):
    sum = 0
    for i in arr:
        sum += i
    f = open(filename, "w")
    f.write(str(sum))
    f.close()
    return

#####################
##   EXERCISE 6    ##
#####################
def line_count(filename):
    count = 0
    f = open(filename)
    arr = f.readlines()
    f.close()
    for i in arr:
        if len(i) >= 10:
            count += 1
    return count

#####################
##   EXERCISE 7    ##
#####################
def odd_nums_md(filename):
    sum = 0
    count = 0
    f = open(filename)
    arr = f.readline().split(",")
    f.close()
    for i in range(len(arr)):
        if i % 2 != 0:
            sum += int(arr[i])
            count += 1
    return sum/count

def exercises():
    while True:
        number = int(input("exercise number: "))
        if number > 0 and number < 8:
            break
        else:
            print("number is not defined")
    if number == 1:
        num = int(input("n = "))
        print(sum(num))
    elif number == 2:
        str = input("str: ")
        pr(str)
    elif number == 3:
        print(prod("files/prod.txt"))
    elif number == 4:
        print(item_count("files/item_count.txt"))
    elif number == 5:
        array = []
        n = int(input("list length: "))
        for i in range(n):
            array.append(int(input("new int = ")))
        sum_arr("files/sum_arr.txt", array)
    elif number == 6:
        print(line_count("files/line_count.txt"))
    elif number == 7:
        print(odd_nums_md("files/odd_nums_md.txt"))

exercises()