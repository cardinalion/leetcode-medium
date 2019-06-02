class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        l = len(nums)
        max_step = 0
        
        for i in range(l):
            if nums[i] == 0:
                if max_step <= i:
                    if i == l-1:
                        return True
                    return False
            else:
                max_step = max(max_step, i+nums[i])
        
        return True
