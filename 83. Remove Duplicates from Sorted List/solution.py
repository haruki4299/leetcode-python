# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        temp = head

        if temp == None:
            return head

        while temp.next != None:
            curVal = temp.val
            nextVal = temp.next.val
            if curVal == nextVal:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head
