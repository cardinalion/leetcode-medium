# first method
# that I wrote in the first place

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
           
        l = len(nums)
        
        count={nums[0]:1}
        
        for i in range(1,l):
            try:
                count[nums[i]] += 1
            except KeyError:
                count[nums[i]] = 1 
            """
            or it can be written as
            count.setdefault(nums[i], 0) += 1
            """
        
        count=sorted(count.items(), key=operator.itemgetter(1), reverse=True)
        
        res = [count[0][0]]
        
        for j in range(1,k):
            res.append(count[j][0])
        
        return res


# second method
# using collections.Counter.most_common()

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [key for key, value in collections.Counter(nums).most_common(k)]
        
        # in python 2
        return zip(*collections.Counter(nums).most_common(k))[0]


# third method
# using heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
            return heapq.nlargest(k, c, c.get) #really cool way to write the key function

        
# fourth method
# using quick select

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        def quick_select(left, right):
                pivot = left
                l, r = left, right
                while l < r:
                    while l < r and counts[r][1] <= counts[pivot][1]:
                        r -= 1
                    while l < r and counts[l][1] >= counts[pivot][1]:
                        l += 1
                    counts[l], counts[r] = counts[r], counts[l]
                counts[left], counts[l] = counts[l], counts[left]

                if l + 1 == k:
                    return counts[:l+1]
                elif l + 1 < k:
                    return quick_select(l + 1, right)
                else:
                    return quick_select(left, l - 1)
                
        c = collections.Counter(nums)
        return [i[0] for i in quick_select(0, len(c) - 1)]
