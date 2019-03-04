class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)

        left = 0
        right = l-1
        
        while right >= left:
            print(nums)
            pos = int((left+right)/2)
            if nums[pos] == target:
                return pos
            l = self.search(nums[left:pos], target)
            r = self.search(nums[pos+1:right+1], target)
            if l == -1:
                return pos+r+1 if r != -1 else -1
            else:
                return l
        
        return -1
