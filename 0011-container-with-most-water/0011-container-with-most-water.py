class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            temp = min(height[l], height[r]) * (r - l)
            res = max(temp, res)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return res
            
