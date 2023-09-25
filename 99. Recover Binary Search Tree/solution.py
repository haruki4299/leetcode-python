# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def inorder(root, list1):
            if root is None:
                return list1
            list1 = inorder(root.left, list1)
            list1.append(root)
            list1 = inorder(root.right, list1)
            return list1


        list1 = inorder(root, [])
        n = len(list1)
        i,j = 1, n-2
        for i in range(1, n):
            if list1[i].val < list1[i-1].val:
                a = list1[i-1]
                break
        b = list1[-1]
        for i in range(n-2, -1, -1):
            if list1[i].val > list1[i+1].val:
                b = list1[i+1]
                break

        a.val,b.val = b.val, a.val
