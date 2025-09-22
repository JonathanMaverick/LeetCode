class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_table = {}
        nums.sort()

        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1

        max_freq = max(hash_table.values())

        total = sum(freq for freq in hash_table.values() if freq == max_freq)

        return total
        

