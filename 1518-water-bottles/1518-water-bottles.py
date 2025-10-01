class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        temp = numBottles
        extra = 0

        while temp >= numExchange:
            extra += temp // numExchange
            temp = (temp // numExchange) + (temp % numExchange) 
        
        return res + extra
            
        