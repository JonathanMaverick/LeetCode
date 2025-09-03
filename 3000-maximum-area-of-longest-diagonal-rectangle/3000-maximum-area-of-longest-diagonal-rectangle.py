import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        temp = 0
        res = 0
        index = 0
        for i in range(len(dimensions)):
            temp = math.sqrt(dimensions[i][0] * dimensions[i][0] + dimensions[i][1] * dimensions[i][1])
            
            if temp > res:
                res = temp
                index = i
            elif temp == res:
                test = dimensions[i][0] * dimensions[i][1]
                if test >= dimensions[index][0] * dimensions[index][1]:
                    index = i

        
        return dimensions[index][0] * dimensions[index][1]