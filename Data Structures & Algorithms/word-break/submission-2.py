class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n

        wordSet = set(wordDict)

        for i in range(n):
            if s[:i+1] in wordSet:
                dp[i] = True
                continue
            for j in range(i):
                if dp[j] == True and s[j+1:i+1] in wordSet:
                    dp[i] = True
                    break
        
        print(dp)
        return dp[-1]
            
