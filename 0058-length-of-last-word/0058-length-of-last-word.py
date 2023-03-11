class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split()
        cnt = len(lst[-1])
            
        return cnt