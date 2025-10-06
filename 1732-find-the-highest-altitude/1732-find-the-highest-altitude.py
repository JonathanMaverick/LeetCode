class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        temp = 0
        for i in range(len(gain)):
            temp += gain[i]
            res = max(res, temp)
        
        return res