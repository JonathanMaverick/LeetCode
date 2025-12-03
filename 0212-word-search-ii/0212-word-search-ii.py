class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = False
        
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.word = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, path = set(), set()

        def dfs(r, c, word, curr):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in path or board[r][c] not in curr.child:
                return
            
            path.add((r,c))
            curr = curr.child[board[r][c]]
            word += board[r][c]
            if curr.word:
                res.add(word)
            
            dfs(r + 1, c, word, curr)
            dfs(r - 1, c, word, curr)
            dfs(r, c + 1, word, curr)
            dfs(r, c - 1, word, curr)
            path.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)
        return list(res)
