class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nums.sort()
        pos = neg = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                pos += 1
            elif 0 > nums[i]:
                neg += 1
        return pos if pos > neg else neg
        