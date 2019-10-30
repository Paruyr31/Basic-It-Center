from random import randint as r
import math as m

################
##  Student   ##
################
class Student():
    def __init__(self, name, surname, age, rating):
        self.name = name
        self.surname = surname
        self.age = age
        self.rating = rating
    def mid_rating(self):
        arr = self.rating
        sum = 0
        count = len(arr)
        for i in arr:
            sum += i
        md = sum//count
        message = "The middle rating for "+str(self.age)+" year old "+self.name+" "+self.surname+" is "+str(md)+"."
        return message

#################
##  Building   ##
#################
class Building():
    def __init__(self, floor, entrance, home):
        self.floor = floor
        self.entrance = entrance
        self.home = home
    def home_count(self):
        homes = self.floor*self.entrance*self.home
        return homes

##################
##  Exercises   ##
##################
class Vector():
    def __init__(self, length):
        self.length = length
        self.arr = []
        for i in range(self.length):
            self.arr.append(r(-20, 20))

    def print_vector(self):
        print(self.arr)

    def ex_211(self):
        sum = 0
        count = 0
        for i in self.arr:
            if i > 0:
                sum += i
                count += 1
        return sum//count

    def ex_214(self):
        sum = 0
        count = 0
        for i in self.arr:
            if i < 0:
                sum += i
                count += 1
        return sum//count

    def ex_216(self):
        prod = 1
        for i in range(len(self.arr)):
            if i % 2 == 0:
                prod *= self.arr[i]
        return prod

    def ex_218(self):
        sum = 0
        for i in range(len(self.arr)):
            if i % 2 != 0:
                sum += m.fabs(self.arr[i])
        return sum

    def ex_220(self):
        pos = 0 # positive numbers count
        neg = 0 # negative numbers count
        for i in self.arr:
            if i >= 0:
                pos += 1
            else:
                neg += 1
        message = str(pos)+" positive and "+str(neg)+" negative numbers."
        return message

    def ex_223(self, a, b):
        count = 0
        for i in self.arr:
            if i > a and i < b:
                count += 1
        return count

    def ex_225(self, t):
        prod = 1
        for i in self.arr:
            if m.fabs(i) < t:
                prod *= i
        return prod

    def ex_227(self, k):
        sum = 0
        count = 0
        for i in range(len(self.arr)):
            if i % k == 0:
                sum += i
                count += 1
        return sum//count

    def ex_229(self):
        prod = 1
        for i in range(len(self.arr)):
            if self.arr[i] - i > 0:
                prod *= self.arr[i]
        return prod

    def ex_230(self, k):
        sum_sqrt = 0
        for i in self.arr:
            if int(i) % k == 0:
                sum_sqrt += m.pow(i ,2)
        md_sqrt = m.sqrt(sum_sqrt)
        return md_sqrt