class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        count = 0
        for i in range(n) :
            count = count ^ start + 2 * i

        return count
