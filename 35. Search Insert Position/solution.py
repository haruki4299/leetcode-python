class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = len(nums)
        for i in range(l):
            if nums[i] >= target:
                return i

        return l
