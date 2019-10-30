import math as m
#####################
##  EXERCISE 201   ##
#####################
def count(num):
    count = 1
    while num//10 != 0:
        num = num//10
        count += 1
    return count
#####################
##  EXERCISE 202   ##
#####################
def sum(num):
    sum = 0
    while num//10 != 0:
        sum += num%10
        num = num//10
    sum += num
    return sum
#####################
##  EXERCISE 203   ##
#####################
def prod(num):
    prod = 1
    while num//10 != 0:
        prod *= num%10
        num = num//10
    prod *= num
    return prod
#####################
##  EXERCISE 204   ##
#####################
def rigth_to_left(num):
    while num//10 != 0:
        res = num%10
        num = num//10
        print(res, end=" ")
    print(num, end=" ")
#####################
##  EXERCISE 205   ##
#####################
def left_to_rigth(num):
    while num%10 != 0:
        c = count(num) - 1
        res = int(num//m.pow(10, c))
        num = int(num%m.pow(10, c))
        print(res, end=" ")
#####################
##  EXERCISE 206   ##
#####################
def reverse(num):
    mode = 0
    while num//10 != 0:
        mode *= 10
        mode += num%10
        num = num//10
    mode*=10
    return mode + num
#####################
##  EXERCISE 207   ##
#####################
def isset_2(num):
    item = 0
    while num//10 != 0:
        item = num%10
        num = num//10
        if item == 2:
            return True
    if num == 2:
        return True
    return False
#####################
##  EXERCISE 208   ##
#####################
def simetric(num):
    arr = []
    while num//10 != 0:
        mode = num%10
        num = num//10
        arr.append(mode)
    arr.append(num)
    for i in arr:
        if arr[0] == i:
            t = True
        else:
            return False
    return t
#####################
##  EXERCISE 209   ##
#####################
def odd(num):
    while num//10 != 0:
        mode = num%10
        num = num//10
        if mode % 2 != 0:
            return True
    if num % 2 != 0:
        return True
    else:
        return False
#####################
##  EXERCISE 210   ##
#####################
def odd_is_even(num):
    sum_odd = 0
    sum_even = 0
    while num//10 != 0:
        c = count(num)
        if c % 2 != 0:
            # all odd
            sum_odd += num%10
        else:
            # all even
            sum_even += num%10
        num = num//10
    sum_odd += num
    return sum_odd, sum_even
