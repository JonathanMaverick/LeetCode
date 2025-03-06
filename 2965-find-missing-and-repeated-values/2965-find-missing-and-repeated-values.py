class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = [0] * (len(grid) * len(grid))
        count = 0
        for row in grid:
            for i in range(len(row)):
                arr[count] = row[i]
                count = count + 1

        double = 0
        missing = 0
        arr.sort()
        print(arr)
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                double = arr[i]

        for i in range(1, len(arr) + 1):  # Expected numbers are from 1 to n
            if i not in arr:  # If a number from 1 to n is missing, mark it as missing
                missing = i
                break

        return [double, missing]

        return double, missing                