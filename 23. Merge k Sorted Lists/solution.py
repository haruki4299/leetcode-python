# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        newList = None
        length = 0
        l = len(lists)
        for i in range(l):
            temp = lists[i]
            while temp != None:
                length += 1
                temp = temp.next

        for i in range(length):
            smallest = 100000
            smallestIndex = -1
            for j in range(l):
                if lists[j] != None:
                    if lists[j].val < smallest:
                        smallest = lists[j].val
                        smallestIndex = j
            if smallestIndex != -1:
                newList = ListNode(smallest,newList)
                lists[smallestIndex] = lists[smallestIndex].next

        # reverse it
        ans = None
        for i in range(length):
            ans = ListNode(newList.val,ans)
            newList = newList.next

        return ans
