class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        left, right, start, end = 0, l-1, -1, -1
        
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] == target:
                start = end = mid
                for i in range(mid-1, left-1, -1):
                    if nums[i] == target:
                        start = i
                for j in range(mid+1, right+1):
                    if nums[j] == target:
                        end = j
                return [start, end]
            if nums[mid] > target:
                return self.searchRange(nums[left: mid], target)
            ret = self.searchRange(nums[mid+1: right+1], target)
            if ret[0] == -1:
                return [-1, -1]
            else:
                return [ret[0]+mid+1, ret[1]+mid+1]
        
        return [start, end]
