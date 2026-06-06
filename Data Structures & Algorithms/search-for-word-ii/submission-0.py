from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build a trie containing every target word.
        for word in words:
            current = root

            for character in word:
                if character not in current.children:
                    current.children[character] = TrieNode()

                current = current.children[character]

            # Store the full word at the final node.
            current.word = word

        rows = len(board)
        columns = len(board[0])
        result = []

        def dfs(row: int, column: int, node: TrieNode) -> None:
            character = board[row][column]

            # Stop if the current board path is not a prefix
            # of any remaining target word.
            if character not in node.children:
                return

            next_node = node.children[character]

            # A complete target word has been found.
            if next_node.word is not None:
                result.append(next_node.word)

                # Prevent the same word from being added again
                # if another board path reaches this trie node.
                next_node.word = None

            # Temporarily mark this cell as visited.
            board[row][column] = "#"

            if row > 0 and board[row - 1][column] != "#":
                dfs(row - 1, column, next_node)

            if row + 1 < rows and board[row + 1][column] != "#":
                dfs(row + 1, column, next_node)

            if column > 0 and board[row][column - 1] != "#":
                dfs(row, column - 1, next_node)

            if column + 1 < columns and board[row][column + 1] != "#":
                dfs(row, column + 1, next_node)

            # Restore the cell so other paths may use it.
            board[row][column] = character

            # Optional optimization:
            # Remove trie branches that can no longer produce a word.
            if not next_node.children and next_node.word is None:
                del node.children[character]

        # Try using every board cell as the first letter.
        for row in range(rows):
            for column in range(columns):
                dfs(row, column, root)

        return result