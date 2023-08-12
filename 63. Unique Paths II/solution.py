class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        A = obstacleGrid
        m = len(A)
        n = len(A[0])
        ans = [[0]*n for x in range(m)]
        if A[0][0] == 1:
            return 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    ans[i][j] = 1
                else:
                    if A[i][j] == 1:
                        ans[i][j] = 0
                    else:
                        if i - 1 >= 0:
                            ans[i][j] += ans[i-1][j]
                        if j - 1 >= 0:
                            print(i,j-1)
                            ans[i][j] += ans[i][j-1]

        return ans[m-1][n-1]
