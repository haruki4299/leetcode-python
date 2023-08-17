class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        a = 0
        b = 0
        mergedList = []
        while a < m or b < n:
            if a == m:
                mergedList.append(nums2[b])
                b += 1
            elif b == n:
                mergedList.append(nums1[a])
                a += 1
            elif nums1[a] > nums2[b]:
                mergedList.append(nums2[b])
                b += 1
            else:
                mergedList.append(nums1[a])
                a += 1
        
        for i in range(m+n):
            nums1[i] = mergedList[i]
