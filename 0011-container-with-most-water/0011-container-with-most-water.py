class Solution:
    def maxArea(self, arr: List[int]) -> int:
        j, k = 0, len(arr) - 1
        max = 0

        for i in range(len(arr)):
            temp = 0
            if arr[j] < arr[k]:
                temp = arr[j] * (k - j)
                j += 1
            else:
                temp = arr[k] * (k - j)
                k -= 1
    
            if max < temp:
                max = temp
        return max

        
    