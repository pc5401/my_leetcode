class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort() # ASC 정렬
        
        for i in range(len(nums)- 2): # 결과값이 3개니까. '-2'
            # 중복된 값 pass
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 간격을 투포인터로 줄이면서 접근
            left, right = i + 1, len(nums) - 1
            while left < right: # 투포인터 범위 초과하기 전까지 
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1 # 더 키워
                elif sum > 0:
                    right -= 1 # 더 줄여
                else: # sum = 0 이다., 찾았다.
                    results.append([nums[i],nums[left],nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
        return results
                    
            
        