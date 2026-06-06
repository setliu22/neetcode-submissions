class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()

            current = current.children[character]

        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            # Reached the end of the search word.
            # Return True only if an inserted word also ends here.
            if index == len(word):
                return node.is_end_of_word

            character = word[index]

            # A dot can match any single character.
            if character == ".":
                for child_node in node.children.values():
                    if dfs(index + 1, child_node):
                        return True

                return False

            # A regular letter must exist in the current node's children.
            if character not in node.children:
                return False

            return dfs(index + 1, node.children[character])

        return dfs(0, self.root)