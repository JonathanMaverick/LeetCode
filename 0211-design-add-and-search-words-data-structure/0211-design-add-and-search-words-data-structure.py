class TrieNode():
    def __init__(self):
        self.child = {}
        self.word = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(curr, j):
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for child in curr.child.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if char not in curr.child:
                        return False
                    curr = curr.child[char]
            return curr.word
        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)