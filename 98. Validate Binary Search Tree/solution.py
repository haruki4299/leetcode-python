# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, maxVal, minVal):
            result = 1
            curVal = root.val
            leftRoot = root.left
            rightRoot = root.right
            print(curVal)
            # Check Validity of left node
            if leftRoot != None:
                if leftRoot.val < curVal and minVal < leftRoot.val:
                    result *= dfs(leftRoot, curVal, minVal)
                else:
                    result *= 0
            # check validity of right node
            if rightRoot != None and result != 0:
                if rightRoot.val > curVal and maxVal > rightRoot.val:
                    result *= dfs(rightRoot, maxVal, curVal)
                else:
                    result *= 0
            return result

        if dfs(root, float('inf'), float('-inf')) == 1:
            return True
        else:
            return False
