# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        ans = ListNode()
        temp = ans
        while list1 != None or list2 != None:
            if list1 == None:
                temp.next = list2
                list2 = None
            elif list2 == None:
                temp.next = list1
                list1 = None
            else:
                if list1.val > list2.val:
                    temp.next = ListNode(list2.val, None)
                    temp = temp.next
                    list2 = list2.next
                else:
                    temp.next = ListNode(list1.val, None)
                    temp = temp.next
                    list1 = list1.next

        return ans.next
