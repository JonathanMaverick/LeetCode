class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        l, r, cz = 0, 0, 0
        res = 0

        while r < len(arr):
            if arr[r] == 0:
                cz += 1
                if cz > k:
                    while arr[l] != 0:
                        l += 1
                    cz -= 1
                    l += 1
            r += 1
            res = max(res, r - l)

        return res
            
        