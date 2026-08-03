class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(strng, frontCount, backCount):
            if backCount > frontCount or frontCount > n:
                return

            if len(strng) == 2 * n:
                ans.append(strng)
                return

            for char in "()":
                if char == "(":
                    dfs(strng + "(", frontCount + 1, backCount)
                else:
                    dfs(strng + ")", frontCount, backCount + 1)

        dfs("", 0, 0)
        return ans