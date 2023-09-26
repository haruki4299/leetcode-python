class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        147|29|56|389
        147|29|56|39|8
        147|29|56 8|39
        147|29|5689|3
        """
        l = len(nums)
        i = l-1
        changed = False
        while i > 0 and changed == False:
            num1 = nums[i-1]
            num2 = nums[i]
            if num1 >= num2:
                i -= 1
            else:
                changed = True
                firstHalf = nums[:i-1]
                secondHalf = nums[i-1:]
                firstElement = nums[i-1]
                secondHalf.sort()
                index = -1
                l2 = len(secondHalf)
                for j in range(l2):
                    if secondHalf[j] == firstElement and secondHalf[j] != secondHalf[j+1]:
                        index = j + 1
                        break
                newSecondHalf = []
                newSecondHalf.append(secondHalf[index])
                secondHalf.remove(secondHalf[index])
                newSecondHalf += secondHalf
                array = firstHalf + newSecondHalf
                for x in range(l):
                    nums[x] = array[x]
        if changed == False:
            nums.sort()
