class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r, cz = 0, 0, 0
        res = 0
        while r < len(nums):
            if nums[r] == 0:
                cz += 1
                if cz > 1:
                    while nums[l] != 0:
                        l += 1
                    l += 1
                    cz -= 1
            r += 1
            res = max(res, r - l)
            
        return max(res, r - l) - 1
                
            