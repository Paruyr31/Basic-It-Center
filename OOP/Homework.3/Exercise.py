from random import randint as r
import math

class Car():
    def __init__(self, color, mass, motor):
        self.color = color
        self.mass = mass
        self.motor = motor
    def character(self):
        print("color:", self.color)
        print("mass:", self.mass)
        print("motor:", self.motor)

class Audi(Car):
    def __init__(self, color, mass, motor, model):
        super().__init__(color, mass, motor)
        self.model = model
    def character(self):
        print(self.color + " Ford " + self.model + " with mass " + str(self.mass) + "(Kg) has motor " + str(self.motor))

class Ford(Car):
    def __init__(self, color, mass, motor):
        super().__init__(color, mass, motor)

"""Polimorphism"""
# a = Audi("red", 2400, 5.5, "TT")
# a.character()

"""Inheritence"""
# f = Ford("blue", 1800, 4.2)
# f.character()

class Exercise():
    def __init__(self, length, pos=None):
        self.set_length(length)
        self.set_pos(pos)
    def set_length(self, length):
        self.__length = length
    def set_pos(self, pos):
        self.__pos = pos
    def get_length(self):
        return self.__length
    def get_pos(self):
        return self.__pos
    def set_matrix(self):
        matrix = []
        for _ in range(self.get_length()):
            arr = []
            for _ in range(self.get_length()):
                arr.append(r(-20, 20))
            matrix.append(arr)
        self.__matrix = matrix
    def get_matrix(self):
        self.set_matrix()
        return self.__matrix
    def print_matrix(self):
        mtr = self.get_matrix()
        for i in range(self.get_length()):
            for j in range(self.get_length()):
                print(mtr[i][j], end="\t")
            print()

    ##################
    ##  Exercises   ##
    ##################

    def ex_432(self):
        self.print_matrix()
        mtr = self.get_matrix()
        n = self.get_length()
        sum = 0
        if self.get_pos().lower() == "up":
            for i in range(n-1):
                for j in range(n-i-1):
                    if (i + j) % 2 != 0:
                        sum += math.pow(mtr[i][j], 2)
            print(math.sqrt(sum))
        elif self.get_pos().lower() == "on here":
            for i in range(n):
                for j in range(n):
                    if i + j == n - 1:
                        if (i + j) % 2 != 0:
                            sum += math.pow(mtr[i][j], 2)
            print(math.sqrt(sum))
    def ex_435(self):
        self.print_matrix()
        mtr = self.get_matrix()
        n = self.get_length()
        count = 0
        for i in range(n-1):
            for j in range(n-i-1):
                if (i + j) % 2 != 0:
                    if int(mtr[i][j]) % 5 == 0:
                        count += 1
        print(count)
    def ex_436(self, a, b):
        self.print_matrix()
        mtr = self.get_matrix()
        n = self.get_length()
        sum = 0
        count = 0
        for i in range(1, n):
            for j in range(i):
                if mtr[i][j] >= a and mtr[i][j] <= b:
                    sum += mtr[i][j]
                    count += 1
        print(sum/count)
    def ex_439(self):
        self.print_matrix()
        mtr = self.get_matrix()
        n = self.get_length()
        prod = 1
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (i + j) % 2 != 0:
                    prod *= mtr[i][j]
        print(prod)
    def ex_440(self):
        self.print_matrix()
        mtr = self.get_matrix()
        n = self.get_length()
        sum = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (i + j) % 2 == 0:
                    sum += mtr[i][j]
        print(sum)
    def ex_442(self):
        self.print_matrix()
        mtr = self.get_matrix()
        n = self.get_length()
        sum = 0
        count = 0
        for i in range(n-1):
            for j in range(n-i-1):
                if mtr[i][j] < 0:
                    sum += mtr[i][j]
                    count += 1
        print(sum/count)
    def ex_445(self, k):
        self.print_matrix()
        mtr = self.get_matrix()
        n = self.get_length()
        count = 0
        for i in range(1, n):
            for j in range(i):
                if math.fabs(mtr[i][j]) > k:
                    count += 1
        print(count)