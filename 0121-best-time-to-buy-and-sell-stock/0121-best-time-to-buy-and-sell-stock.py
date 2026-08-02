class Solution:
    def maxProfit(self, prices):
        n = len(prices)

        dp = [[0, 0] for _ in range(n)]

        # Day 0
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):

            # Don't hold stock
            dp[i][0] = max(
                dp[i-1][0],             # do nothing
                dp[i-1][1] + prices[i]  # sell today
            )

            # Hold stock
            dp[i][1] = max(
                dp[i-1][1],             # continue holding
                -prices[i]               # buy today
            )

        return dp[n-1][0]