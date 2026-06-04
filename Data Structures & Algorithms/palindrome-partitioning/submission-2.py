# very very straightforward

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        path = []

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start: int) -> None:
            if start == len(s):
                result.append(path.copy())
                return

            for end in range(start, len(s)):
                if not is_palindrome(start, end):
                    continue

                path.append(s[start:end + 1])
                dfs(end + 1)
                path.pop()

        dfs(0)
        return result