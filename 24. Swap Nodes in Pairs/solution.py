# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        rev = None
        while temp != None:
            val1 = temp.val
            temp = temp.next
            if temp != None:
                rev = ListNode(temp.val, rev)
                temp = temp.next
            rev = ListNode(val1, rev)
        
        ans = None
        while rev != None:
            ans = ListNode(rev.val, ans)
            rev = rev.next
        return ans
