import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nm = np.array(matrix).flatten()
        left, right =0, len(nm) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nm[pivot] == target:
                return True
            elif nm[pivot] > target:
                right = pivot - 1
            elif nm[pivot] < target:
                left = pivot + 1
            
        return False
         