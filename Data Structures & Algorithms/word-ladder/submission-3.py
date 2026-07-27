from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        wordQueue = deque([[beginWord, 1]])

        while wordQueue:
            currWord, currLen = wordQueue.popleft()
            print(f"{currWord}, {currLen}")
            for i in range(len(beginWord)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    newWord = currWord[:i] + char + currWord[i+1:]
                    print(f"{i}, {currWord[:i]}, {char}, {currWord[i+1:]}")
                    if newWord == endWord:
                        return currLen+1
                    if newWord in wordSet:
                        wordQueue.append([newWord, currLen+1])
                        wordSet.remove(newWord)
        
        return 0