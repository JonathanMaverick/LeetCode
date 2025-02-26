class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        new_arr = set(nums)
        new_arr = list(new_arr)
        new_arr.sort()
        print(new_arr)

        longest = 0
        curr_longest = 0
        for i in range(len(new_arr) - 1):
            if new_arr[i] + 1 == new_arr[i+1]:
                longest = longest + 1
            else:
                if curr_longest < longest:
                    curr_longest = longest
                longest = 0 
        
        return max(curr_longest, longest) + 1