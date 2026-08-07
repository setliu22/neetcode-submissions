class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = float("inf")

        index = 0

        n = len(prices)

        ans = 0

        while index < n:
            currMin = min(currMin, prices[index])
            
            ans = max(ans, prices[index] - currMin)

            index += 1
        
        return ans