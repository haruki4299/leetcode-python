class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue = []
        l = len(s)
        for i in range(l):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                queue.append(s[i])
            elif s[i] == ')':
                if queue == [] or queue.pop(-1) != '(':
                    return False
            elif s[i] == '}':
                if queue == [] or queue.pop(-1) != '{':
                    return False
            elif s[i] == ']':
                if queue == [] or queue.pop(-1) != '[':
                    return False

        if queue != []:
            return False

        return True
