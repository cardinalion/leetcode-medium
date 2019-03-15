class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l == 0:
            return [[]]
        if l == 1:
            return [[], nums]
        ret = [[], [nums[0]]]
        
        for i in range(1, l):
            for j in range(pow(2, i)):
                ret.append(ret[j]+[nums[i]])
        
        return ret
