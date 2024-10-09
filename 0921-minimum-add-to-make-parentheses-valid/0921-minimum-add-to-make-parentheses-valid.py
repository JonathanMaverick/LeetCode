class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        nyawa = 0
        hutang = 0
        for i in range(len(s)):
            if s[i] == '(':
                nyawa += 1
            elif s[i] == ')':
                if nyawa > 0:
                    nyawa -= 1
                else:
                    hutang += 1
        if hutang == 0:
            return nyawa
        elif hutang != 0 and nyawa != 0:
            return nyawa + hutang
        else:
            return hutang
                