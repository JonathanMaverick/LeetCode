class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            k = i + 1
            l = len(nums) - 1 
            while k < l:
                res = nums[i] + nums[k] + nums[l]
                if res == 0:
                    result.append([nums[i], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif res > 0:
                    l -= 1 
                elif res < 0:
                    k += 1
        return result
            
            