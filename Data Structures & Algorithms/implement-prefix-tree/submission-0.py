class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()

            current = current.children[character]

        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root

        for character in word:
            if character not in current.children:
                return False

            current = current.children[character]

        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for character in prefix:
            if character not in current.children:
                return False

            current = current.children[character]

        return True