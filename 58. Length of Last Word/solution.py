class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = len(s)
        count = 0

        for i in range(l):
            char = s[l-1-i]
            if char != ' ':
                for j in range(i,l):
                    char = s[l-1-j]
                    if char == ' ':
                        return count
                    count += 1
                    if j == l - 1:
                        return count
        
        return count
