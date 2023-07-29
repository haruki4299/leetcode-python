# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 1
        temp = head
        while temp.next != None:
            count += 1
            temp = temp.next
        
        temp = head

        if count == n:
            return head.next
            
        remove = count - n

        i = 0
        while remove - 1 > i:
            temp = temp.next
            i += 1
        print(temp.val)
        if temp.next != None:
            temp.next = temp.next.next
        else:
            temp.next = None

        return head


