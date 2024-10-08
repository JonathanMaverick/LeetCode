class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                ans[i] = nums[i] + ans[i - 1]
            else :
                ans[i] = nums[i]

        return ans
        