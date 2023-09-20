# Code hint from vanAmsen LeetCode
# sliding window to find max length array
# Personal solution TLE 79/90 testcases
"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        minCount = float('inf')
        l = len(nums)
        for i in range(l+1):
            sum1 = 0
            count = 0
            if minCount < i+1:
                continue
            for k in range(i):
                sum1 += nums[k]
                count += 1
            if sum1 == x:
                if minCount > count:
                    minCount = count
            if sum1 > x:
                    break
            j = l-1
            while i <= j and sum1 < x and count <= minCount:
                sum1 += nums[j]
                count += 1
                j = j - 1
                if sum1 == x:
                    if minCount > count:
                        minCount = count
        if minCount == float('inf'):
            return -1
        else:
            return minCount
"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        l = len(nums)
        target = total - x
        if target == 0:
            return l
        maxLen = 0
        curSum = 0
        left = 0

        for right in range(l):
            curSum += nums[right]
            while left <= right and curSum > target:
                curSum -= nums[left]
                left += 1
            if curSum == target:
                maxLen = max(maxLen, right - left + 1)
        
        return l - maxLen if maxLen else -1
