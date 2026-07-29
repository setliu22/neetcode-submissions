class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)

        if s[0] == "0":
            return 0
        elif n == 1:
            return 1
        
        # dp: number of ways up to this character (make 2nd digit if in range 10-26, make single digit if in range 1-9)

        dp = [0] * n

        dp[0] = 1

        if int(s[:2]) < 27 and int(s[1]) != 0:
            dp[1] = 2
        elif int(s[:2]) >= 27 and int(s[1]) != 0:
            dp[1] = 1
        elif int(s[:2]) < 27 and int(s[1]) == 0:
            dp[1] = 1
        else:
            dp[1] = 0

        for i in range(2, n):
            # if two digit possible, add the number of ways from 2 before
            twoDigit = dp[i-2] if (int(s[i-1:i+1]) < 27) and (int(s[i-1:i+1]) >= 10) else 0
            print(int(s[i-1:i+1]))
            # if one digit possible (not 0), add the number of ways from 1 before
            oneDigit = dp[i-1] if (int(s[i]) != 0) else 0
            dp[i] = twoDigit+oneDigit
        
        print(dp)
        return dp[-1]