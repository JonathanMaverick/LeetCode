class Solution:
    def maxVowels(self, s: str, sw: int) -> int:
        vowels = {'a', 'i', 'u', 'e', 'o'}

        j, k =  0, sw 
        temp = sum(ch in vowels for ch in s[:sw])
        res = temp
        if res == sw:
            return sw
            
        while k < len(s):
            temp = temp - (s[j] in vowels) + (s[k] in vowels)
            res = max(res, temp)
            if sw == res:
                return sw 
            j, k = j + 1, k + 1

        return res
            
        