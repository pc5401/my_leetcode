class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        # 이중 반복문 구조
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 뺀다.
                top = stack.pop()
                
                if not len(stack):
                    break
                    
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                res += distance * waters
            
            stack.append(i)
        
        return res