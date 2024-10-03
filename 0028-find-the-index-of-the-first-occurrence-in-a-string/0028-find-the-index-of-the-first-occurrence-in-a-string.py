class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack : 
            return -1
        i = 0
        for x in range(len(haystack)):
            substr = haystack[x : x + len(needle)]
            if substr == needle:
                return x