# -*- coding: utf-8 -*-


class S:
    def __init__(self):
        pass

    def isPalindromic(self, arr):
        if len(arr) == 0:
            return False
        if len(arr) == 1:
            return True
        left = 0
        right = len(arr) - 1
        while left <= right:
            if arr[left] != arr[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

    def longPalindromicSubstring(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return arr
        dp = [[False for _ in range(len(arr))] for _ in range(len(arr))]
        maxlen = 0
        res = ''
        right = 0
        while right < len(arr):
            dp[right][right] = True
            left = 0
            while left < right:
                dp[left][right] = (right - left < 2 or dp[left+1][right-1]) and arr[left] == arr[right]
                if dp[left][right] and right - left > maxlen:
                    maxlen = right - left
                    res = arr[left:right+1]
                left += 1
            right += 1
        return res

if __name__=='__main__':
    arr = 'gabagabadcaba'
    S = S()
    print 's is palindromic?', S.isPalindromic(arr)
    print 's contains substring:',S.longPalindromicSubstring(arr)

