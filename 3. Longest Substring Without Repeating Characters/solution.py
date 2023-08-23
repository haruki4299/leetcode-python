class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        index = 0
        l = len(s)
        while index < l:
            seen = []
            cur = index
            length = 0
            while cur < l:
                char = s[cur]
                if char not in seen:
                    length += 1
                    seen.append(char)
                else:
                    break
                cur += 1
            if longest < length:
                longest = length
            index += 1

        return longest
