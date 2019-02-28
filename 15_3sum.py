class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = 0
        l = len(nums)
        i = 1
        count0 = 0
        while i < l: 
            if nums[i] == nums[i-1]:
                if nums[i] != 0:
                    count += 1
                else:
                    count0 += 1
                    del nums[i]
                    l -= 1
                    i -= 1
            else:
                count = 0
            if count > 1:
                del nums[i]
                l -= 1
            else:
                i += 1
        
        ret = []

        if count0 > 1:
            ret.append([0,0,0])
            
        for m in range(l-2):
            if nums[m] > 0:
                break
            if i > 0 and nums[m] == nums[m-1]:
                continue
            j = m+1
            k = l-1
            while k > j:
                s = nums[m] + nums[j] + nums[k] 
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    ret.append([nums[m], nums[j], nums[k]])
                    if j < k and nums[j] == nums[j+1]:
                        j += 1
                    if k > j and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        
        return ret
