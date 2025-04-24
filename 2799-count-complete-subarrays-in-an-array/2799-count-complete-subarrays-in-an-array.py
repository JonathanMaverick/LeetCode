class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_nums = set(nums)
        total_distinct = len(distinct_nums)
        count = 0

        for i in range(len(nums)):
            current_set = set()
            for j in range(i, len(nums)):
                current_set.add(nums[j])
                if len(current_set) == total_distinct:
                    count += (len(nums) - j)
                    break
        
        return count