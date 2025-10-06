class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp, tp = 0, 0
        while len(t) > tp and len(s) > sp:
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
            else:
                tp += 1
        
        return sp == len(s)
            
            