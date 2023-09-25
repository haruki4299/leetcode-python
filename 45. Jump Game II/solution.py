class Solution:
    def jump(self, nums: List[int]) -> int:
        reachableInd = []
        l = len(nums)
        goal = l-1
        for i in range(l):
            reachableInd.append(i+nums[i])
        curIndex = 0
        moves = 0
        while curIndex < goal:
            moves += 1
            possibleMax = nums[curIndex]
            bestIndex = curIndex + 1
            for i in range(1,possibleMax+1):
                if curIndex+i >= goal:
                    bestIndex = goal
                    break
                if reachableInd[bestIndex] < reachableInd[curIndex+i]:
                    bestIndex = curIndex+i
            curIndex = bestIndex
        return moves
