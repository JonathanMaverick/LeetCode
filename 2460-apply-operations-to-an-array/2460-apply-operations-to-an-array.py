class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        nums_arr = [num for num in nums if num is not 0]
        zero_count = nums.count(0)
        
        return nums_arr + zero_count * [0] 