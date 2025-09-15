class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                right_empty = (i == (len(flowerbed) - 1) or flowerbed[i + 1] == 0)
                left_empty = (i == 0 or flowerbed[i - 1] == 0)

                if right_empty and left_empty:
                    flowerbed[i] = 1
                    n -= 1
            
            if n == 0:
                return True
        
        return False