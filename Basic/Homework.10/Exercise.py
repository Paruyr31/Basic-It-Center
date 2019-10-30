import math
import random

"""block input"""
def input_l():
    l = int(input("list length: ")) # length
    return l

def input_q():
    while True: # question
        do = input("please input: 'down' or 'on here'? ")
        if do == "down" or do == "on here":
            break
        else:
            print("wrong answer!")
    return do

def input_k():
    k = int(input("k = ")) # num1
    return k

def input_a():
    a = int(input("a = ")) # num2
    return a
"""block end"""

def gen_matrix(len, fl = True):
    array = []
    for i in range(len):
        array.append([])
    for i in range(len):
        for j in range(len):
            rand = random.random()*random.randint(-10, 10)
            if fl:
                if rand < 0:
                    rand = str(rand)
                    rand = float(rand[:5])
                elif rand == 0:
                    rand = str(rand)
                    rand = 0
                else:
                    rand = str(rand)
                    rand = float(rand[:4])
            else:
                if rand < 0:
                    rand = str(rand)
                    rand = int(float(rand[:4]))
                elif rand == 0:
                    rand = str(rand)
                    rand = 0
                else:
                    rand = str(rand)
                    rand = int(float(rand[:3]))
            array[i].append(rand)
    print()
    for i in range(len):
        for j in range(len):
            print(array[i][j], end="\t")
        print()
    print()
    return array

def ex_434(length, question):
    arr = gen_matrix(length)
    sum = 0
    if question == "down":
        for i in range(1, length):
            for j in range(length-1, length):
                item = math.fabs(arr[i][j])
                if item >= 5.4 and item <= 15.3:
                    sum += item
    else:
        for i in range(length):
            for j in range(length):
                if i + j == length - 1:
                    item = math.fabs(arr[i][j])
                    if item >= 5.4 and item <= 15.3:
                        sum += item

    return sum

def ex_436(length):
    arr = gen_matrix(length)
    sum = 0
    count = 0
    print("[a; b]")
    a = int(input("a = "))
    b = int(input("b = "))

    for i in range(1, length):
        for j in range(i):
            item = arr[i][j]
            if item >= a and item <= b:
                sum += item
                count += 1

    return sum/count

def ex_437(length, question):
    arr = gen_matrix(length, False)
    md_sqrt = 0
    if question == "down":
        for i in range(1, length):
            for j in range(length-1, length):
                item = arr[i][j]
                if item == int(item):
                    md_sqrt += math.pow(item, 2)
    else:
        for i in range(length):
            for j in range(length):
                if i + j == length - 1:
                    item = arr[i][j]
                    if item == int(item):
                        md_sqrt += math.pow(item, 2)

    return math.sqrt(md_sqrt)

def ex_438(length):
    arr = gen_matrix(length)
    count = 0
    for i in range(1, length):
        for j in range(i):
            item = arr[i][j]
            if item >= 0 and i % 2 == 0 or j % 2 == 0:
                count += 1

    return count

def ex_439(length):
    arr = gen_matrix(length)
    prod = 1
    for i in range(length-1):
        for j in range(i+1, length):
            item = arr[i][j]
            if (i + j) % 2 != 0:
                prod *= item

    return prod

def ex_440(length):
    arr = gen_matrix(length)
    sum = 0
    for i in range(length-1):
        for j in range(i+1, length):
            item = arr[i][j]
            if (i + j) % 2 == 0:
                sum += item

    return sum

def ex_441(length):
    arr = gen_matrix(length)
    md_sqrt = 0
    for i in range(length-1):
        for j in range(i+1, length):
            item = math.pow(arr[i][j], 2)
            md_sqrt += item

    return math.sqrt(md_sqrt)

def ex_442(length):
    arr = gen_matrix(length)
    sum = 0
    count = 0
    for i in range(length-1):
        for j in range(length-i-1):
            item = arr[i][j]
            if item < 0:
                sum += item
                count += 1

    return sum/count

def ex_445(length, k):
    arr = gen_matrix(length)
    count = 0
    for i in range(1, length):
        for j in range(i):
            item = math.fabs(arr[i][j])
            if item > k:
                count += 1

    return count

def ex_447(length, question, a):
    arr = gen_matrix(length)
    prod = 1
    if question == "down":
        for i in range(1, length):
            for j in range(length-1, length):
                item = arr[i][j]
                if item < a:
                    prod *= item
    else:
        for i in range(length):
            for j in range(length):
                if (i + j) == length - 1:
                    item = arr[i][j]
                    if item < a:
                        prod *= item

    return prod

def ex_449(length):
    arr = gen_matrix(length)
    sum = 0
    for i in range(length-1):
        for j in range(length-1-i):
            item = arr[i][j]
            if int(item) % 4 == 0:
                sum += item

    return sum

def ex_450(length):
    arr = gen_matrix(length)
    sum = 0
    for i in range(1, length):
        for j in range(length-i, length):
            item = arr[i][j]
            m = item - int(item)
            sum += m

    return sum

def decorator_1(func_name, val):
    answer = func_name(val)
    if answer != None and bool(str(answer)):
        return True
    return False
def decorator_2(func_name, val1, val2):
    answer = func_name(val1, val2)
    if answer != None and bool(str(answer)):
        return True
    return False
def decorator_3(func_name, val1, val2, val3):
    answer = func_name(val1, val2, val3)
    if answer != None and bool(str(answer)):
        return True
    return False