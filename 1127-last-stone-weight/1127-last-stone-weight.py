class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            if s2 > s1:
                res = s1 - s2
                heapq.heappush(stones, res)
        
        stones.append(0)
        return abs(stones[0])
                
        