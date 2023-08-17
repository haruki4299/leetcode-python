class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        l = len(nums)
        rem = []
        num = 0

        for i in range(l):
            if nums[i] != val:
                num += 1
                rem.append(nums[i])

        for j in range(num):
            nums[j] = rem[j]
            

        return num
