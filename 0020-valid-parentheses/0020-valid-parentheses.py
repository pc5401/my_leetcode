class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ")":"(",
            "]" : "[",
            "}" : "{"
        }
        
        for i in s:
            if i not in dic:
                stack.append(i)
            elif not stack or dic[i] != stack.pop():
                return False

        return len(stack) == 0
        