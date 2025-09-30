class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = nums
        counter = 1
        for i in range(len(nums)):
            for j in range(len(nums) - counter):
                res[j] = (res[j] + res[j + 1])%10
            counter += 1
        return res[0]