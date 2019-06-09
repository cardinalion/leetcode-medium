# O(n^2)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        l = len(nums)
        
        def check_left(lnums: List[int], value: int) -> bool:
            for j in lnums:
                if j < value:
                    return True
            return False
        
        def check_right(rnums: List[int], value: int) -> bool:
            for k in rnums:
                if k > value:
                    return True
            return False
            
        
        for i in range(1, l-1):
            start = 0
            lresult, rresult = check_left(nums[start:i], nums[i]), check_right(nums[i+1:], nums[i])
            if lresult and rresult:
                return True
            if not lresult and not rresult:
                return False
            if lresult:
                start = i
            
        return False


# Refered to leetcode discussion
# O(n)

class Solution:
    def increasingTriplet(nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
