class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Forward
        # Find most profit before each day
        profitsB = []
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
            profitsB.append(maxProfit)
        

        # Other way
        # Find max profit after each day
        profitsA = []
        maxPrice = prices[-1]
        maxProfit = 0
        l = len(prices)
        for i in range(l-1,-1,-1):
            maxPrice = max(maxPrice, prices[i])
            maxProfit = max(maxProfit, maxPrice - prices[i])
            profitsA.append(maxProfit)
        
        # Now find best
        maxProfitOfTwo = 0
        for i in range(l):
            maxProfitOfTwo = max(maxProfitOfTwo, profitsB[i] + profitsA[l-i-1])
            
        return maxProfitOfTwo
