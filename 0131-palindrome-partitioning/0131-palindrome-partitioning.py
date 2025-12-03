class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i, j):
            if j >= len(s):
                if i == j:
                    res.append(part.copy())
                return
            
            if self.isPali(i, j, s):
                part.append(s[i:j + 1])
                dfs(j + 1, j + 1)
                part.pop()
            
            dfs(i, j + 1)
        dfs(0, 0)
        return res
            
    
    def isPali(self, l, r, s):
        while l < r:
            if not s[l] == s[r]:
                return False
            l += 1
            r -= 1
        return True
                
        