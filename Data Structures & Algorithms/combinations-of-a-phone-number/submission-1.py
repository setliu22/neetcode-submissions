class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        path = []

        def dfs(i: int) -> None:
            if i == len(digits):
                result.append("".join(path))
                return

            for letter in phone[digits[i]]:
                path.append(letter)  # choose
                dfs(i + 1)           # explore
                path.pop()           # undo the choice

        dfs(0)
        return result