# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ansList = None
        revList = None
        l = 0
        temp = head
        #reverse the list.
        while temp != None:
            revList = ListNode(temp.val, revList)
            l += 1
            temp = temp.next
        remainder = l % k
        iterations = l // k
        temp = revList
        for i in range(remainder):
            ansList = ListNode(temp.val, ansList)
            temp = temp.next
        for i in range(iterations):
            localRev = None
            for j in range(k):
                localRev = ListNode(temp.val, localRev)
                temp = temp.next
            for m in range(k):
                ansList = ListNode(localRev.val, ansList)
                localRev = localRev.next
        return ansList
