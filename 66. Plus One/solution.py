class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        l = len(digits) 
        i = 0
        while i < l:
            if digits[l-1-i] != 9:
                digits[l-1-i] += 1
                break
            else:
                digits[l-1-i] = 0
                if i == l-1:
                    return [1] + digits

            i += 1

        return digits
