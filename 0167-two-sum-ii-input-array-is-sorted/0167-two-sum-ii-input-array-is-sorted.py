class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = 0
        k = len(numbers) - 1
        while j < k: 
            if numbers[j] + numbers[k] > target:
                k -= 1
            elif numbers[j] + numbers[k] < target:
                j += 1 
            else:
                return [j + 1, k + 1]