#O(n) solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        a = {}
        n = len(nums)
        for i in range(n):
            b = nums[i]
            diff = target - b
            if diff in a:
                return [a[diff], i]
            else:
                a[b] = i
