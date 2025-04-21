class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_prefix = 0
        max_prefix = 0
        current = 0

        for diff in differences:
            current += diff
            min_prefix = min(min_prefix, current)
            max_prefix = max(max_prefix, current)

        min_x = lower - min_prefix
        max_x = upper - max_prefix

        return max(0, max_x - min_x + 1)