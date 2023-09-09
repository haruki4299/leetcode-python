class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l == 1:
            return 0

        if k >= l // 2:
            max_profit = 0
            for i in range(1, l):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit

        dp = [[0] * l for _ in range(k + 1)]

        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, l):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])
        return dp[k][l - 1]

        """
        dp = [[0] * l for _ in range(2)]  # Use a rolling array to optimize memory usage

        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, l):
                dp[i % 2][j] = max(dp[i % 2][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[(i - 1) % 2][j] - prices[j])
                
        return dp[k % 2][l - 1]
        """
