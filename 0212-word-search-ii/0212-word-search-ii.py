class TrieNode:
    def __init__(self):
        self.word = False
        self.child = {}
        
    def addWords(self, word):
        curr = self
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.word = True 
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        root = TrieNode()
        
        path = set()
        res = set()
        for w in words:
            root.addWords(w)

        def dfs(r, c, curr, word):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r,c) in path or board[r][c] not in curr.child:
                return 
                
            path.add((r,c))
            curr = curr.child[board[r][c]]
            word += board[r][c]
            if curr.word:
                res.add(word)

            dfs(r + 1, c, curr, word)
            dfs(r - 1, c, curr, word)
            dfs(r, c + 1, curr, word)
            dfs(r, c - 1, curr, word)
            path.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)
                
                         
        