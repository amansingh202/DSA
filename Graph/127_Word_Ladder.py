## leetcode 127. Word Ladder

from typing import List
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st = set(wordList)

        if endWord not in st:
            return 0
        
        if beginWord in st:
            st.remove(beginWord)

        q = deque([(beginWord, 1)])

        l = len(beginWord)

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps
            
            chars = list(word)

            for i in range(l):
                original = chars[i]

                for k in range(26):
                    ch = chr(ord('a') + k)

                    chars[i] = ch
                    nxt = ''.join(chars)

                    if nxt in st:
                        st.remove(nxt)
                        q.append((nxt, steps + 1))

                chars[i] = original
        return 0
    
sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # 5
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))        # 0

        
        

        