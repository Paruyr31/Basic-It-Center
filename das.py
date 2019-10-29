def binary_search(arr, element):
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = (l+r) // 2

        if arr[mid] == element:
            return True
        if element > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return False
import math
arr = [1,5,7,10,17,20,30]
print(binary_search(arr,31))

import random
import time
def gen_arr(n):
    arr_n = n
    arr = []
    for i in range(arr_n):
        arr.append(random.randint(1,100))
    return arr
def f(a):
    return a**2

def a(a):
    return a+3


arr = [1,2,3,4]
arr2 = [5,6,7,8]
res = list(map(lambda a,b: a+b,arr,arr2))
res1 = list(map(a,arr))
a = lambda a,b: a+b
res3 = list(filter(lambda a: a < 10,arr))
res3 = list(map(lambda a: a*a,res3))
print(a(5,7))
print(res)
print(res1)
print(res3)
arr3 = gen_arr(10000)



import re

s = "The sun is shining."
pattern = "shining.$"
d = "abcdea"

res = re.findall(pattern,s)
print(res)