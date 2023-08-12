class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        lcp = ""
        l = len(strs)
        cont = True

        while cont:
            if strs[0] != "":
                char = strs[0][0]
            else:
                break
            for i in range(l):
                if strs[i] == "":
                    cont = False
                    break
                if strs[i][0] != char:
                    cont = False
                    break
                else:
                    strs[i] = strs[i][1:len(strs[i])]
            if cont == True:
                lcp += str(char)

        return lcp
