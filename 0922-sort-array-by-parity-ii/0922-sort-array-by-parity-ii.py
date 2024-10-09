class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [0] * (len(nums) // 2)
        odd = [0] * (len(nums) // 2)

        evenCount = 0
        oddCount = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even[evenCount] = nums[i]
                evenCount+=1
            else :
                odd[oddCount] = nums[i]
                oddCount+=1
        
        sortedeven = even.sort()
        sortedodd = odd.sort()
        res = [0] * len(nums)

        for i in range(len(nums) // 2):
            res[i * 2] = even[i]
            res[(i * 2) + 1] = odd[i]

        return res; 
