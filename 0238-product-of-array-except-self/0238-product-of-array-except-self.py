class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        v= 1
        for i in range(len(nums)):
            res.append(v)
            v = v * nums[i]
            
        v = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * v
            v = v * nums[i]
            
        return res