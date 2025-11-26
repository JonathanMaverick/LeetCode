from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t)
        currCounter = Counter()
        l = 0
        required = len(tCounter)
        formed = 0

        res = (float("inf"), 0, 0)
        
        for r, ch in enumerate(s):
            currCounter[ch] += 1

            if ch in t and currCounter[ch] == tCounter[ch]:
                formed += 1
            
            while formed == required:
                if (r - l + 1) < res[0]:
                    res = (r - l + 1, l, r)
                temp = s[l]
                currCounter[temp] -= 1
                if temp in t and currCounter[temp] < tCounter[temp]:
                    formed -= 1
                l += 1

        if res[0] == float("inf"):
            return ""
        else:
            return s[res[1]:res[2] + 1]
                
        