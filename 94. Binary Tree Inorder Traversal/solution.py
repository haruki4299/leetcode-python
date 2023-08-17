# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def recInorder(ans, root):
            if root.left != None:
                recInorder(ans, root.left)
            ans.append(root.val)
            if root.right != None:
                recInorder(ans, root.right)

        ans = []
        if root == None:
            return ans
        recInorder(ans,root)

        return ans
