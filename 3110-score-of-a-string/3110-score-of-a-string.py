class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if i + 1 != len(s):
                res = res + abs(ord(s[i]) - ord(s[i + 1]))
        
        return res