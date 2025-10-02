class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty, full, res = numBottles, 0, numBottles
        while empty >= numExchange:
            empty -= numExchange
            numExchange += 1
            full += 1
            if empty < numExchange:
                empty += full
                res += full
                full = 0

        return res