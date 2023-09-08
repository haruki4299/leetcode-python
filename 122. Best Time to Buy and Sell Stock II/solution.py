class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        k = 0
        l = len(prices)
        if l == 1:
            return 0
        while k < l - 1:
            diff = prices[k+1] - prices[k]
            if diff > 0:
                profit += diff
            k += 1
        return profit
