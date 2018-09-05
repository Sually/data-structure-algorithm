# -*- coding: utf-8 -*-

class S:

    def __init__(self):
        pass

    def binaryFind(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            pivote = (left + right) // 2
            if target < arr[pivote]:
                right = pivote - 1
            elif target > arr[pivote]:
                left = pivote + 1
            else:
                return 'Yes'
        return 'No'

if __name__ == '__main__':
    arr = range(1, 14, 1)
    S = S()
    for i in arr:
        print S.binaryFind(arr, i)