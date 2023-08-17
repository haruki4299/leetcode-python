# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def recTreeCompare(p,q):
            a = 1
            b = 1
            if p.val != q.val:
                return 0
            else:
                if (p.left == None and q.left != None) or (p.left != None and q.left == None):
                    a = 0
                elif p.left != None and q.left != None:
                    a = recTreeCompare(p.left,q.left)
                else:
                    a = 1

                if (p.right == None and q.right != None) or (p.right != None and q.right == None):
                    b = 0
                elif p.right != None and q.right != None:
                    b = recTreeCompare(p.right,q.right)
                else:
                    b = 1
            
            return a * b

        if p == None and q == None:
            return True
        elif p != None and q != None:
            if recTreeCompare(p,q) != 1:
                print(recTreeCompare(p,q))
                return False
            else:
                return True
        else:
            return False


