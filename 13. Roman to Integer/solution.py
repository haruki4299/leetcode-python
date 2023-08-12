class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        nums = {
             "I":1,
             "V":5,
             "X":10,
             "L":50,
             "C":100,
             "D":500,
             "M":1000
        }

        l = len(s)
        ans = 0
        i = 0
        while i < l:
            if i + 1 == l:
                ans += nums[s[i]]
            elif nums[s[i]] >= nums[s[i+1]]:
                ans += nums[s[i]]
            else:
                if s[i+1] == "M":
                    ans += 900
                elif s[i+1] == "D":
                    ans += 400
                elif s[i+1] == "C":
                    ans += 90
                elif s[i+1] == "L":
                    ans += 40
                elif s[i+1] == "X":
                    ans += 9
                elif s[i+1] == "V":
                    ans += 4
                i += 1
            i += 1

        return ans
