class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # combinations = backtracking
        n = len(digits)
        ans = []

        if n == 0:
            return []

        dict1 = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(index, strng):
            if index == n:
                ans.append(strng)
                return

            for char in dict1[digits[index]]:
                dfs(index+1, strng+char)


        dfs(0, "")

        return ans