class Solution:
    def maxVowels(self, s: str, sw: int) -> int:
        vowels = {'a', 'i', 'u', 'e', 'o'}
        if len(s) == 1:
            if s in vowels:
                return 1
            else:
                return 0

        j, k =  0, sw 
        temp = sum(1 for ch in s[j:k] if ch in vowels)
        res = temp
        while k < len(s):
            temp = temp - (s[j] in vowels) + (s[k] in vowels)
            res = max(res, temp)
            if sw == res:
                return sw 
            j, k = j + 1, k + 1

        return res
            
        