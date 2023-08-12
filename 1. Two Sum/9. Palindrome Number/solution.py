class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = 0
        temp = x
        if temp < 0:
            return False

        while temp != 0:
            reverse = reverse * 10 + temp % 10
            temp = temp // 10

        if reverse == x:
            return True
        else:
            return False
