class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        priority_queue = [(0, 0, 0)] 

        while priority_queue:
            distance, current_row, current_col = heapq.heappop(priority_queue)
            
            if current_row == num_rows - 1 and current_col == num_cols - 1:
                return distance
                
            for delta_row, delta_col in directions:
                new_row, new_col = current_row + delta_row, current_col + delta_col
                
                if (new_row >= num_rows or new_col >= num_cols or 
                    new_row < 0 or new_col < 0 or 
                    visited[new_row][new_col]):
                    continue
                    
                visited[new_row][new_col] = True
                heapq.heappush(priority_queue, (max(distance + 1, grid[new_row][new_col] + 1), new_row, new_col))

        return -1