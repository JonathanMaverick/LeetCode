class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        texts = text.split(" ")
        count = 0

        for t in texts:
            for b in brokenLetters:
                if b in t:
                    count += 1
                    break

        return len(texts) - count