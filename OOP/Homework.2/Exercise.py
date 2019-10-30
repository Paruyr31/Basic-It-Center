import math

class Vector():
    def __init__(self, length):
        self.set_length(length)
        self.__arr = []
    def set_length(self, length):
        self.__length = length
    def get_length(self):
        return self.__length
    def set_arr(self):
        for i in range(self.get_length()):
            self.__arr.append(r(-20, 20))
    def get_arr(self):
        self.set_arr()
        return self.__arr

rand_arr = Vector(11).get_arr()

##################
##  Exercises   ##
##################

class Solution():
    def __init__(self, arr):
        self.set_arr(arr)
        self.array = self.get_arr()
    def set_arr(self, arr):
        self.__arr = arr
    def get_arr(self):
        return self.__arr
    def get_len(self):
        self.__length = len(self.get_arr())
        return self.__length

    def ex_312(self):
        print(self.array)
        arr = []
        for i in range(0, len(self.array), 2):
            a = self.array[i:i+2]
            a = int(math.fabs(min(a)))
            arr.append(a)
        return arr
    def ex_314(self):
        print(self.array)
        arr = self.array
        i = 0
        while i < len(arr):
            if arr[i] > 0:
                arr.insert(i+1, 0)
            i += 1
        return arr
    def ex_316(self):
        print(self.array)
        arr = []
        mid = (min(self.array)+max(self.array))/2
        for i in self.array:
            i = int(math.fabs(i))
            if i < mid:
                arr.append(i)
        return arr
    def ex_320(self):
        print(self.array)
        arr = self.array
        f_max = arr.index(max(arr))
        arr.remove(arr[f_max])
        for i in range(len(arr)):
            if arr[i] == min(arr):
                e_min = i
        arr.remove(arr[e_min])
        return arr
    def ex_322(self):
        print(self.array)
        arr = self.array
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i+1, 0)
                arr.insert(i+2, 0)
                i += 3
                continue
            i += 1
        return arr
    def ex_323(self):
        print(self.array)
        array = self.array
        arr = []
        mid = (min(array)+max(array))/2
        for i in array:
            if i > mid:
                arr.append(i)
        return arr
    def ex_325(self):
        print(self.array)
        arr = self.array
        Max = max(arr)
        i = arr.index(Max)
        arr[0], arr[i] = arr[i], arr[0]
        return arr
    def ex_326(self):
        print(self.array)
        arr = self.array
        for i in range(len(arr)//2):
            e = -(i+1)
            s = i
            arr[s], arr[e] = arr[e], arr[s]
        return arr
    def ex_327(self):
        print(self.array)
        array = self.array
        arr = []
        for i in range(len(array)):
            if array[i] == min(array):
                arr.append(i)
        return arr
    def ex_329(self):
        print(self.array)
        array = self.array
        arr = []
        for i in range(len(array)):
            sum = 0
            for j in range(i):
                sum += array[j]
            arr.append(sum)
        return arr
    def ex_330(self):
        print(self.array)
        array = self.array
        arr = []
        i = 0
        while i < len(array):
            if array[i] % 2 == 0:
                arr.append(array[i])
                array.remove(array[i])
                continue
            i += 1
        arr.extend(array)
        return arr
    def ex_332(self):
        print(self.array)
        arr = self.array
        min_2 = int(math.pow(min(arr), 2))
        max_3 = int(math.pow(max(arr), 3))
        ma = arr.index(max(arr))
        mi = arr.index(min(arr))
        arr[ma], arr[mi] = min_2, max_3
        return arr