class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0    
        for i, nums in enumerate(nums):
            right_sum = totalSum - leftSum - nums
            if right_sum == leftSum:
                return i
            leftSum += nums
        return -1