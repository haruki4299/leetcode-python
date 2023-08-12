class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        seen = []
        l = len(nums)
        num = l
        for i in range(l):
            x = nums[i]
            if x in seen:
                num -= 1
            else:
                seen.append(x)
        
        for j in range(num):
            nums[j] = seen[j]

        return num
