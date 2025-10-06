class Solution:
    def maxOperations(self, nums: List[int], target: int) -> int:
        j, k, operation = 0, len(nums) - 1, 0
        nums.sort()
        while (j < k):
            total = nums[j] + nums[k]
            if total == target:
                j += 1
                k -= 1
                operation += 1
            elif total > target:
                k -= 1
            elif total < target:
                j += 1
        return operation