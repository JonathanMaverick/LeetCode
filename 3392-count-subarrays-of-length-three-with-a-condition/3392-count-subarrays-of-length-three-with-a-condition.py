class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        counter = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                counter += 1
            
        return counter