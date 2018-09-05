# -*- coding: utf-8 -*-
import random
import sys
sys.setrecursionlimit(10000)  # set recursion depth

# avg=O(nlogn) best=O(nlogn) worst=O(n*n) space=O(logn)~O(n)
class S:

    def __init__(self):
        pass

    def quickSort(self, arr):
        if not arr:
            return []
        if len(arr) == 1:
            return arr
        pivote = arr[0]
        left = self.quickSort([i for i in arr[1:] if i < pivote])
        right = self.quickSort([i for i in arr[1:] if i >= pivote])
        return left + [pivote] + right

if __name__ == '__main__':
    arr = [random.randint(0, 110) for _ in range(15)]
    print arr
    S = S()
    print S.quickSort(arr)