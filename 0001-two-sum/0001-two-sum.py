class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i, n in enumerate(nums):
            data[n] = i
            
        for i, n in enumerate(nums):
            if target - n in data and i != data[target - n]:
                return [i, data[target - n]]