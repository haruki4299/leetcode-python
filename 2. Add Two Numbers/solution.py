# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        ans = None
        carry = 0
        while l1 != None or l2 != None:
            sum1 = carry
            carry = 0
            if l1 != None:
                sum1 += l1.val
                l1 = l1.next
            if l2 != None:
                sum1 += l2.val
                l2 = l2.next
            if sum1 >= 10:
                carry = 1
            sum1 = sum1 % 10
            ans = ListNode(sum1, ans)
        if carry == 1:
            ans = ListNode(1, ans)
        
        ans2 = None
        while ans != None:
            ans2 = ListNode(ans.val, ans2)
            ans = ans.next

        return ans2
