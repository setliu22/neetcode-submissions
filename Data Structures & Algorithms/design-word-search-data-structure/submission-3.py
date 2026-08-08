class WordDictionary:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        n = len(word)
        curr = self.tree

        for index in range(n):
            char = word[index]

            if index == n - 1:
                char += '*'
            
            if char not in curr:
                curr[char] = {}
            
            curr = curr[char]

    def search(self, word: str) -> bool:
        n = len(word)
        
        def dfs(index, currLevel):
            if index == n - 1:
                if word[index] == '.':
                    for char in currLevel:
                        if '*' in char:
                            return True
                    return False
                if word[index] + '*' in currLevel:
                    return True
                else:
                    return False
            if word[index] == '.' and currLevel:
                for key in currLevel:
                    if dfs(index + 1, currLevel[key]):
                        return True
                return False
            elif word[index] in currLevel:
                return dfs(index + 1, currLevel[word[index]])
            else:
                return False
        
        return dfs(0, self.tree)
