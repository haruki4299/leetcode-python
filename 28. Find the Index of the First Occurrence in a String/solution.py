class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        first = -1
        l1 = len(haystack)
        l2 = len(needle)
        
        for i in range(l1):
            if haystack[i] == needle[0]:
                first = i
                ind = first
                for j in range(l2):
                    if ind >= l1:
                        return -1
                    elif needle[j] != haystack[ind]:
                        first = -1
                        break
                    else:
                        ind += 1
                if first != -1:
                    return first

        return first
