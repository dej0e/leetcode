class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for idx, c in enumerate(word):
            if c == ".":
                for key in cur.children.keys():
                    if self.searchFromNode(cur.children[key], word, idx + 1):
                        return True
                return False
            elif c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def searchFromNode(self, node: TrieNode, word: str, startIndex) -> bool:
        cur = node
        for i in range(startIndex, len(word)):
            c = word[i]
            if c == ".":
                for key in cur.children.keys():
                    if self.searchFromNode(cur.children[key], word, i + 1):
                        return True
                return False
            elif c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
