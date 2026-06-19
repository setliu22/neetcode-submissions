"""
THE REPEATING WORDS IS LOWKEY BROKEN

if using recursive we can just memoize whether we're able to reach a certain index

this seems inefficient because of the branching options but go through each character and see if from that character to the end of the word there are words (make 1 if so and also mark where the word ends). then, do a pass from the front explore all possible branching options. so start with n see where n words end, if that index returns 1 go to where those words end, branching possibilities etc

Both branches reach index 7. Without remembering anything, you process everything after index 7 twice.

dfs method w/ remembering whether each index can reach the end

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        n = len(s)

        ends = [[] for _ in range(n)]

        for start in range(n):
            for end in range(start + 1, n + 1):
                if s[start:end] in words:
                    ends[start].append(end)

        memo = {}

        def canReachEnd(index):
            if index == n:
                return True

            if index in memo:
                return memo[index]

            for next_index in ends[index]:
                if canReachEnd(next_index):
                    memo[index] = True
                    return True

            memo[index] = False
            return False

        return canReachEnd(0)

DFS with memoization is dynamic programming.
Bottom-up DP stores the same answers but fills them with loops instead of recursion.

The question is always:

Can the substring starting at index 7 be broken into words?

iterative way:

At index 4:
"code" is a word
and dp[8] is True (empty string after index 8)
therefore dp[4] = True

basically at each i store the answer to the central question of this problem

it helps a lot we can reuse words so we can spam a 4-length word
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[n] = True

        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n + 1):
                word = s[start:end]

                if word in words and dp[end]:
                    dp[start] = True
                    break

        return dp[0]