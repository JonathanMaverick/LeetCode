class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        res = 0
        left = max_count = 0
        
        for i in range(len(nums)):
            if nums[i] == max_element:
                max_count += 1
            while max_count == k:
                res += len(nums) - i
                if nums[left] == max_element:
                    max_count -= 1
                left += 1
        
        return res
