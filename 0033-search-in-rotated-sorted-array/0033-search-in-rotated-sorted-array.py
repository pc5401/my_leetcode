class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        n = len(nums)
        idx = nums.index(min(nums))
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            v = (mid + idx) % n
            
            if nums[v] < target:
                left = mid + 1
            elif nums[v] > target:
                right = mid - 1
            else:
                return v
        return -1