class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[1]*i for i in range(1,numRows+1)]

        for i in range(1, numRows+1):
            for j in range(1,i-1):
                if i == 1 or i == 2:
                    print(f'i:{i}')
                    break

                if j-1 >= 0 and i-1 >= 0:
                    lst[i-1][j] = lst[i-2][j] + lst[i-2][j-1]
                    
                        
        return lst