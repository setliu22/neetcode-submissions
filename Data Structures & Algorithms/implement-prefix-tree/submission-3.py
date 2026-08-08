# use * after a character to indicate it's the end of a word
# use [0] and use [1] to check for *
# lowkey just add another 26 possibilities for chars with a * after

class PrefixTree:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
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

        curr = self.tree

        for index in range(n):
            char = word[index]
            if index == n - 1:
                if char + '*' not in curr:
                    return False
                else:
                    return True
            elif char not in curr:
                return False

            curr = curr[char]

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)

        curr = self.tree

        for index in range(n):
            char = prefix[index]

            if char not in curr and char + '*' not in curr:
                return False

            if char in curr:
                curr = curr[char]
            else:
                break
        
        return True
        
        