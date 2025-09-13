class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return_list = []
        for i in range(len(nums)):
            if i == 0:
                return_list.append(nums[i])
            else:
                return_list.append(nums[i] + return_list[i - 1])
            
        return return_list