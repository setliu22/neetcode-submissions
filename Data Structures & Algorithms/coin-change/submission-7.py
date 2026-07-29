class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1

        dp = [0] * (amount+1)

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for currCoin in range(amount+1):
            if dp[currCoin] == 0:
                currMin = float("inf")
                for coin in coins:
                    if currCoin-coin > -1:
                        currMin = min(currMin, dp[currCoin-coin])
                
                dp[currCoin] = currMin+1
        
        return dp[-1] if dp[-1] != float("inf") else -1