class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """

        def sumOfn(n):
            ans = 0
            for i in range(1,n+1):
                ans += i
            return ans

        # Think more mathematically
        ans = 0
        for i in range(1,n+1):
            if i == 1:
                ans = 1
            else:
                ans = ans * sumOfn(((i-1)*2)+1)

        mod = 10**9 + 7

        return ans % mod
