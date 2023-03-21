class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            v = target - n
            
            if v in nums[i+1:]: return [nums.index(n), nums[i+1:].index(v) + (i+1)]