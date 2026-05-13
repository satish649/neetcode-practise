class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        if beginWord == endWord:
            return 0
        
        
        queue = deque([(beginWord, 1)])
        seen =set(beginWord)

        def getNeighbors(word):
            neighbors = []
            ascii_a = ord('a')

            for i in range(len(word)):
                prefix = word[0:i]
                suffix = word[i+1:]
                for j in range(26):
                    c_char = chr(ascii_a + j)
                    if word[i] == c_char:
                        continue
                    new_word =  prefix + c_char + suffix
                    # print(f"new_word: {new_word}, i: {i}, beginWord[:i]: {prefix}, c_char: {c_char}, last word part: {beginWord[i+1:]}")
                    if new_word in wordSet and new_word not in seen:
                        # print(f"new_word: {new_word}, i: {i}, beginWord[:i]: {prefix}, c_char: {c_char}, last word part: {beginWord[i+1:]}")
                        neighbors.append(new_word)
            
            # print(f"neighbors: {neighbors}")
            return neighbors

        # min_moves = 0
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                (c_word, level) = queue.popleft()
                # print(f'Word explored: {c_word}')
                if c_word == endWord:
                    return level
                for neighbor in getNeighbors(c_word):
                    # print(f'Neighbor word: {neighbor}')
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, level+1))
        
        return 0
        
                    
        