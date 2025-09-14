class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_amount = 0
        while (left != right):
            current_height = min(height[left], height[right])
            amount = current_height * (right - left)
            if amount > max_amount:
                max_amount = amount
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_amount