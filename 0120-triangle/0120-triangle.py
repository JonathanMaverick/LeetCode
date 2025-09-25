class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        max = 0
        j = 0
        for i in range(len(triangle)):
            if i == 0:
                max = max + triangle[i][j]
                continue 
            
            if triangle[i][j] > triangle[i][j + 1]:
                j += 1
            max = max + triangle[i][j] 
            
        return max
            

            
            
            