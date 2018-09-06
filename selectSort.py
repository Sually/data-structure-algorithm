# -*- coding: utf-8 -*-
import random

class S:

    def __init__(self):
        pass

    def selectSort(self, arr):
        for i in range(len(arr)):
            small = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[small]:
                    arr[j], arr[small] = arr[small], arr[j]
        return arr


if __name__=='__main__':
    arr = [random.randint(1, 100) for _ in range(10)]
    print arr
    S = S()
    print S.selectSort(arr)