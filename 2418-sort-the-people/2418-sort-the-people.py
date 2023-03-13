class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lst = []
        for i,j in sorted(zip(heights,names), key=lambda x : -x[0]):
            lst.append(j)
        return lst