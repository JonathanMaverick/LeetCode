class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.recursion(n, memo)

    def recursion(self, n:int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo: 
            memo[n] = self.recursion(n - 1, memo) + self.recursion(n - 2, memo)
        return memo[n] 

        