from random import randint as r


class Solution():
    def __init__(self, n):
        self.set_length(n)

    def set_length(self, n):
        self.__n = n

    def get_length(self):
        return self.__n

    def vector(self):
        arr = []
        for _ in range(self.get_length()):
            arr.append(r(-20, 20))
        return arr

    def ex_281(self):
        x = self.vector()
        print(x)
        y = list(filter(lambda i: i > 0, x))
        return y

    def ex_282(self):
        x = self.vector()
        print(x)
        y = list(filter(lambda i: i != 0, x))
        return y

    def ex_283(self):
        x = self.vector()
        print(x)
        y = list(filter(lambda i: i % 2 != 0, x))
        return y

    def ex_284(self, a, b):
        x = self.vector()
        print(x)
        y = list(filter(lambda i: i >= a and i <= b, x))
        return y

    def ex_285(self, p):
        x = self.vector()
        print(x)
        y = list(filter(lambda i: i % p == 0, x))
        return y

    def ex_286(self):
        x = self.vector()
        print(x)
        y = list(filter(lambda i: i % 2 == 0, x))
        return y

    def ex_290(self):
        x = self.vector()
        print(x)
        y = list(filter(lambda i: x.index(i) != i, x))
        return y


p = Solution(10)
print(p.ex_290())