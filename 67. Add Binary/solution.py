class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        la = len(a)
        lb = len(b)
        l = 0
        if la > lb:
            l = la
        else:
            l = lb
        
        a1 = ""
        for i in range(l-la):
            a1 += "0"
        a1 = a1 + a
        

        b1 = ""
        for i in range(l-lb):
            b1 += "0"
        b1 = b1 + b

        a1 = str(a1)
        b1 = str(b1)
        ans = ""
        c = 0
        for i in range(l):
            num = int(a1[l-1-i]) + int(b1[l-1-i]) + c
            c = 0
            if num == 2:
                ans = "0" + ans
                c = 1
            elif num == 1:
                ans = "1" + ans
            elif num == 0:
                ans = "0" + ans
            elif num == 3:
                ans = "1" + ans
                c = 1
        if c == 1:
            ans = "1" + ans

        return ans
