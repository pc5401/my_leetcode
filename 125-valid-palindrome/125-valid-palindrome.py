class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [_ for _ in s if _.isalpha() or _.isdigit()]
        reversed_lst = lst[::-1]
        print(lst, reversed_lst)
        result = True
        j = 0
        for i in lst:
            if i.lower() != reversed_lst[j].lower():
                result = False
                break
            else:
                j += 1

        return result
        