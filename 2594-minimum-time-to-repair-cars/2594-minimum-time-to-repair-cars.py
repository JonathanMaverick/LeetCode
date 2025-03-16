class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = min(ranks) * cars * cars
        print(left, right)

        def can_repair_all(time):
            tcr = 0
            for rank in ranks:
                cr = int((time / rank) ** 0.5)
                tcr += cr
                if tcr >= cars:
                    return True
            return False

        while left < right:
            mid = (left + right) // 2
            if can_repair_all(mid):
                right = mid
            else:
                left = mid + 1

        return left
