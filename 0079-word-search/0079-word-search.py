class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, r, c): 
            if i == len(word):
                return True
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or word[i] != board[r][c] or board[r][c] == '#':
                return False
            board[r][c] = '#'
            res = (
                dfs(i + 1, r + 1, c) or
                dfs(i + 1, r - 1, c) or
                dfs(i + 1, r, c + 1) or
                dfs(i + 1, r, c - 1)
            )
            board[r][c] = word[i]
            return res
            
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(0, i, j):
                    return True
        return False
            