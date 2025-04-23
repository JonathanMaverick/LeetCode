class Solution:
    def countLargestGroup(self, n: int) -> int:
        array = 37 * [0]
        for i in range(1, n+1):
            key = sum([int(x) for x in str(i)])
            array[key] += 1
        
        max_value = max(array)
        count = sum(1 for x in array if x == max_value)
        return count
