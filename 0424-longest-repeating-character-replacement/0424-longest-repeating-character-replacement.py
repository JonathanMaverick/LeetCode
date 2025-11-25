class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for char in charSet:
            count = l = 0
            for r in range(len(s)):
                if char == s[r]:
                    count += 1
                while (r - l + 1) - count > k:
                    if char == s[l]:
                        count -= 1
                    l += 1
            
                res = max(res, (r - l + 1))

        return res
                    
                     
            
        
        