from collections import deque
from string import ascii_lowercase
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        def get_neighbors(word):
            res = []
            for i in range(len(word)):
                for c in ascii_lowercase:
                    if c == word[i]:
                        continue
                    mod_word = word[:i] + c + word[i+1:]
                    if mod_word in wordSet:
                        res.append(mod_word)
            return res

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            word, turn = queue.popleft()
            for w in get_neighbors(word):
                if w == endWord:
                    return turn + 1
                if w in visited:
                    continue
                queue.append((w, turn + 1))
                visited.add(w)

        return 0
