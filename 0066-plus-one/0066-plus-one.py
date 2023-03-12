class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        cnt, idx = 0, 0
        while idx < len(digits):
            cnt += digits[-idx-1] * (10**idx)
            idx += 1
        
        res = []
        for s in str(cnt):
            res.append(int(s))
        
        return res