class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        buy = 0
        sell = 1
        max_profit = 0
        while sell < l:
            profit = prices[sell] - prices[buy]
            if profit < 0:
                buy += 1
                if sell == buy:
                    sell += 1
            else:
                if profit > max_profit:
                    max_profit = profit
                sell += 1
        return max_profit
        """
        l = len(prices)
        maxProfit = 0
        for i in range(l):
            buy = prices[i]
            for j in range(i,l):
                sell = prices[j]
                profit = sell - buy
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit
        """
