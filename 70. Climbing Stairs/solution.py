class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # a_n = a_n-1 + a_n-2
        # a_1 = 1, a_2 = 2

        a_y = 2
        a_z = 1

        if n == 1:
            return a_z
        if n == 2:
            return a_y
        
        a_x = 0
        for i in range(3,n+1):
            a_x = a_y + a_z
            a_z = a_y
            a_y = a_x

        return a_x
