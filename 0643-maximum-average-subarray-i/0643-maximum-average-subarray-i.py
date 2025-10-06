class Solution:
    def findMaxAverage(self, nums: List[int], sw: int) -> float:
        n = len(nums)
        j, k, res = 0, sw, 0
        temp = sum(nums[j : k])
        res = temp / sw
        while (k < n):
            temp = temp - nums[j] + nums[k]
            res = max(res, temp / sw)
            j += 1
            k += 1

        return res
            
            
            