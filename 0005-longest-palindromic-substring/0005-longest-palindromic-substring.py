class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        
        def func(left:int, right:int) -> str:
            # 범위를 범어나지 않고
            #  Palindromic 유지하는 녀석들
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1:right]
        
        res = ""
        for i in range(len(s)-1):
            res = max(res, func(i,i+1), func(i,i+2),key=len)
            
        return res
        