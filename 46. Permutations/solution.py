class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ans = []
        def helperPermute(ans, permutation: List[int], array, l):
            if l == 0:
                ans.append(permutation)
            else:
                for i in range(l):
                    copyPerm = permutation[:]
                    copyPerm.append(array[i])
                    copy = array[:]
                    copy.remove(array[i])
                    helperPermute(ans, copyPerm, copy, l-1)
        helperPermute(ans, [], nums, l)
        print(ans)
        return ans
