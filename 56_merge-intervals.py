import functools
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        l = len(intervals)
        if l < 2:
            return intervals
        
        @functools.cmp_to_key
        def mycmp(x: List[int], y:List[int]):
            return x[0]-y[0]
        
        intervals.sort(key=mycmp)
        
        res = []
        tmp = intervals[0]
        
        for i in range(1, l):
            if tmp[1] < intervals[i][0]:
                res.append(tmp)
                tmp = intervals[i]
                continue
            tmp = [tmp[0], max(intervals[i][1], tmp[1])]
        
        res.append(tmp)
        return res
