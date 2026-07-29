class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        total = 0

        for i in range(n):
            dp[i][i] = True
            total += 1
                
        for i in range(0, n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                total += 1
                
        for length in range(3, n+1):
            #print(f"length {length}")
            for start in range(0, n-(length)+1):
                #print(f"{s[start]} {s[start+length-1]}")
                #print(f"{dp[start+1][start+length-2]}")
                if s[start] == s[start+length-1] and dp[start+1][start+length-2]:
                    dp[start][start+length-1] = True
                    total += 1
        
        return total
        
