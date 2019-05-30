class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l = len(nums)
        if l > 1:
            lst = []
            for i in range(l-1, 0, -1):
                lst.append(nums[i])
                if nums[i] > nums[i-1]:
                    tmp = nums[i-1]
                    lst.append(tmp)
                    lst.sort(reverse=True)
                    digit = lst[0]
                    for j in lst:
                        if j < digit and j > tmp:
                            digit = j
                    nums[i-1] = digit
                    lst.remove(digit)
                    for k in range(i, l):
                        nums[k] = lst.pop()
                    break
                if i == 1:
                    lst.append(nums[0])
                    lst.sort(reverse=True)
                    for k in range(l):
                         nums[k] = lst.pop()
           
