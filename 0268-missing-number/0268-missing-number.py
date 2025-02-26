class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                continue
            else:
                return nums[i] + 1
        
        return nums[len(nums) - 1] + 1
        