class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        sums = sum(nums)
        remainder = sums % p

        if sums % p == 0 : 
            return remainder

        pos = {0: -1}
        sumP, Len = 0, n

        for i, x in enumerate(nums):
            sumP = (sumP + x) % p
            y = (sumP-remainder+p) % p
            print(y)

            if y in pos :
                Len = min(Len, i - pos[y])
            pos[sumP]=i
        return -1 if Len == n else Len