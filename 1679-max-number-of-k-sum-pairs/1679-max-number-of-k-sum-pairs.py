class Solution:
    def maxOperations(self, nums: List[int], target: int) -> int:
        nums.sort()
        j, k = 0, len(nums) - 1
        operation = 0
        while (j < k):
            if nums[j] + nums[k] == target:
                j += 1
                k -= 1
                operation += 1
            elif nums[j] + nums[k] > target:
                k -= 1
            elif nums[j] + nums[k] < target:
                j += 1
        return operation