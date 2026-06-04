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

        def dfs(i: int, current: str) -> None:
            if i == len(digits):
                result.append(current)
                return

            for letter in phone[digits[i]]:
                dfs(i + 1, current + letter)

        dfs(0, "")
        return result