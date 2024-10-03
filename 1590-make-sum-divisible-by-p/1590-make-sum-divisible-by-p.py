class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        prefixSum = [0 for i in range(n + 1)]
        min = n+1

        if sum(nums)%p == 0:
            return 0


        for i in range (0, n) : 
            prefixSum[i] = nums[i]
            for j in range(0,n):
                if i == j:continue
                prefixSum[i] = prefixSum[i] + nums[j]
                print(f"prefix sum: {prefixSum[i]}, {n-j-1}")    
                if prefixSum[i] % p == 0:
                    if min > n-j-1:
                        min = n-j-1
        if min == n + 1:
            return -1   
        else:
            return min