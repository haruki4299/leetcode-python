class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def dfs(left, right, ans, s):
            if left == 0 and right == 0:
                ans.append(s)
            elif left == right:
                s = s + "("
                dfs(left - 1, right, ans, s)
            elif left < right:
                if left > 0:
                    s1 = s + "("
                    dfs(left - 1, right, ans, s1)
                if right > 0:
                    s2 = s + ")"
                    dfs(left, right-1, ans, s2)


        
        ans = []
        dfs(n,n,ans,"")
        return ans
        
