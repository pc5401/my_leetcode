class Solution:
    def isPalindrome(self, x: int) -> bool:
        v = str(x)
        vv = v[::-1]
        if v==vv:
            return True
        else:
            return False
        