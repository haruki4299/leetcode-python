class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        i = 0
        while True:
            i += 1
            if i * i > x:
                return i - 1
