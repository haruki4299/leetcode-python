class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        m = len(nums1)
        n = len(nums2)

        i = 0
        j = 0

        if (m+n) % 2 == 1:
            median = (m + n + 1) // 2
            k = 1
            while k < median:
                if i >= m:
                    j += 1
                elif j >= n:
                    i += 1
                elif nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
                k += 1
            if i >= m:
                return nums2[j]
            elif j >= n:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                return nums1[i]
            else:
                return nums2[j]
        else:
            median = (m + n) // 2
            k = 1
            while k < median:
                if i >= m:
                    j += 1
                elif j >= n:
                    i += 1
                elif nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
                k += 1

            median1 = 0
            median2 = 0
            if i >= m:
                median1 = nums2[j]
                j += 1
            elif j >= n:
                median1 = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                median1 = nums1[i]
                i += 1
            else:
                median1 = nums2[j]
                j += 1
            
            if i >= m:
                median2 = nums2[j]
            elif j >= n:
                median2 = nums1[i]
            elif nums1[i] < nums2[j]:
                median2 = nums1[i]
            else:
                median2 = nums2[j]
            
            return (median1 + median2) / 2.0
            
