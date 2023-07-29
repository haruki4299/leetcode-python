class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        startIndex = 0
        length = len(nums) - 1
        if length < 2:
            return []
        ans = []
        nums.sort()

        while startIndex < length - 2:
            first = nums[startIndex]
            if first >= 0 and first > target:
                break
            secondIndex = startIndex + 1
            while secondIndex < length - 1:
                second = nums[secondIndex]
                if second >= 0 and first + second > target:
                    break
                thirdIndex = secondIndex + 1
                while thirdIndex < length:
                    third = nums[thirdIndex]
                    if third >= 0 and first + second + third > target:
                        break
                    fourthIndex = thirdIndex + 1
                    while fourthIndex <= length:
                        fourth = nums[fourthIndex]
                        if fourth > 0 and first + second + third + fourth > target:
                            break
                        if first + second + third + fourth == target:
                            list1 = [first,second,third,fourth]
                            if list1 not in ans:
                               ans.append(list1)
                            break
                        fourthIndex += 1
                    thirdIndex += 1
                secondIndex +=1
            startIndex += 1
        return ans
