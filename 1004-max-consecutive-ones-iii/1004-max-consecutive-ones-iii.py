class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        a, b = 0, 0
        count_zero = 0
        maxi = 0
        while b < len(arr):
            if arr[b] == 0:
                count_zero += 1
                while count_zero > k:
                    if arr[a] == 0:
                        count_zero -= 1
                    a += 1
            b += 1
            maxi = max(maxi, b - a)
        return maxi
             
            
